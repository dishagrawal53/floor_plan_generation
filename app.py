import pickle
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from shapely.geometry import MultiPolygon, Polygon, Point
from shapely import affinity
import copy
import gradio as gr
import geopandas as gpd
from typing import List, Dict, Any, Tuple, Optional
import os

# ============================================================
# UTILITY FUNCTIONS
# ============================================================

CATEGORY_COLORS: Dict[str, str] = {
    "living": "#d9d9d9",
    "bedroom": "#66c2a5",
    "bathroom": "#fc8d62",
    "kitchen": "#8da0cb",
    "door": "#e78ac3",
    "window": "#a6d854",
    "wall": "#ffd92f",
    "front_door": "#a63603",
    "balcony": "#b3b3b3"
}

def normalize_keys(plan: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize common key typos"""
    if "balacony" in plan and "balcony" not in plan:
        plan["balcony"] = plan.pop("balacony")
    return plan

def get_geometries(geom_data: Any) -> List[Any]:
    """Safely extract individual geometries from single/multi/collections."""
    if geom_data is None:
        return []
    if isinstance(geom_data, (Polygon,)):
        return [] if geom_data.is_empty else [geom_data]
    if isinstance(geom_data, (MultiPolygon,)):
        return [g for g in geom_data.geoms if g is not None and not g.is_empty]
    return []

def centroid(poly):
    """Centroid for Polygon/MultiPolygon"""
    if isinstance(poly, Polygon):
        return poly.centroid
    if isinstance(poly, MultiPolygon) and len(poly.geoms) > 0:
        largest = max(poly.geoms, key=lambda p: p.area)
        return largest.centroid
    return Point(-1e6, -1e6)

def plot_plan(plan: Dict[str, Any],
              categories: Optional[List[str]] = None,
              colors: Dict[str, str] = CATEGORY_COLORS,
              ax: Optional[plt.Axes] = None,
              legend: bool = True,
              title: Optional[str] = None,
              tight: bool = True) -> plt.Axes:
    """Plot a single plan with colored layers."""
    plan = normalize_keys(plan)
    if categories is None:
        categories = ["living","bedroom","bathroom","kitchen","door","window","wall","front_door","balcony"]

    geoms, color_list, present = [], [], []
    for key in categories:
        geom = plan.get(key)
        if geom is None:
            continue
        parts = get_geometries(geom)
        if not parts:
            continue
        geoms.extend(parts)
        color_list.extend([colors.get(key, "#000000")] * len(parts))
        present.append(key)

    if not geoms:
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_aspect("equal", adjustable="box")
        ax.set_axis_off()
        if title:
            ax.set_title(title)
        return ax

    gseries = gpd.GeoSeries(geoms)
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    gseries.plot(ax=ax, color=color_list, edgecolor="black", linewidth=0.5)
    ax.set_aspect("equal", adjustable="box")
    ax.set_axis_off()

    if title:
        ax.set_title(title)

    if legend:
        from matplotlib.patches import Patch
        uniq_present = list(dict.fromkeys(present))
        handles = [Patch(facecolor=colors.get(k, "#000000"), edgecolor="black", label=k.replace("_"," ")) for k in uniq_present]
        ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(1,1), frameon=False)

    if tight:
        plt.tight_layout()
    return ax

# ============================================================
# DATABASE CLASS
# ============================================================

class FloorPlanDatabase:
    def __init__(self, pkl_path):
        print("Loading dataset...")
        if not os.path.exists(pkl_path):
            raise FileNotFoundError(f"Dataset not found at {pkl_path}. Please upload ResPlan.pkl")
        
        with open(pkl_path, "rb") as f:
            self.data = pickle.load(f)
        print(f"Loaded {len(self.data)} floor plans")

        for plan in self.data:
            normalize_keys(plan)

        self.bedroom_index = defaultdict(list)
        self.bathroom_index = defaultdict(list)
        self.area_sorted = []
        self._build_indexes()

    def _count_rooms(self, room_geom):
        if room_geom is None or room_geom.is_empty:
            return 0
        if hasattr(room_geom, 'geoms'):
            return len(room_geom.geoms)
        return 1

    def _build_indexes(self):
        print("Building search indexes...")
        for idx, plan in enumerate(self.data):
            bedroom_count = self._count_rooms(plan.get('bedroom'))
            self.bedroom_index[bedroom_count].append(idx)

            bathroom_count = self._count_rooms(plan.get('bathroom'))
            self.bathroom_index[bathroom_count].append(idx)

            area = plan.get('area', 0)
            self.area_sorted.append((area, idx))

        self.area_sorted.sort()
        print("Indexes built successfully!")

    def search_plans(self, bedrooms=None, bathrooms=None,
                     min_area=None, max_area=None,
                     has_kitchen=True, limit=10):

        candidate_indices = set(range(len(self.data)))

        if bedrooms is not None:
            bedroom_matches = set(self.bedroom_index.get(bedrooms, []))
            candidate_indices &= bedroom_matches

        if bathrooms is not None:
            bathroom_matches = set(self.bathroom_index.get(bathrooms, []))
            candidate_indices &= bathroom_matches

        if min_area is not None or max_area is not None:
            area_matches = set()
            for area, idx in self.area_sorted:
                if min_area and area < min_area:
                    continue
                if max_area and area > max_area:
                    break
                area_matches.add(idx)
            candidate_indices &= area_matches

        if has_kitchen:
            kitchen_matches = set()
            for idx in candidate_indices:
                plan = self.data[idx]
                kitchen_geom = plan.get('kitchen')
                if kitchen_geom and not kitchen_geom.is_empty:
                    kitchen_matches.add(idx)
            candidate_indices &= kitchen_matches

        results = []
        for idx in candidate_indices:
            plan = self.data[idx]
            score = 100.0
            results.append((idx, plan, score))

        results.sort(key=lambda x: x[2], reverse=True)
        return results[:limit]

    def get_plan(self, idx):
        return self.data[idx]


# ============================================================
# VASTU COMPLIANCE CLASS
# ============================================================

class VastuCompliance:
    def __init__(self):
        self.zones = {
            'north': (337.5, 22.5),
            'north_east': (22.5, 67.5),
            'east': (67.5, 112.5),
            'south_east': (112.5, 157.5),
            'south': (157.5, 202.5),
            'south_west': (202.5, 247.5),
            'west': (247.5, 292.5),
            'north_west': (292.5, 337.5)
        }

        self.ideal_placements = {
            'kitchen': ['south_east'],
            'bedroom': ['south_west', 'west', 'south'],
            'living': ['north', 'north_east', 'east'],
            'bathroom': ['north_west', 'west'],
            'entrance': ['north', 'east', 'north_east'],
            'balcony': ['north', 'east', 'north_east'],
        }

    def apply_vastu(self, plan):
        print("\n🕉️ Applying Vastu Shastra Principles...")
        vastu_plan = copy.deepcopy(plan)

        room_positions = self._calculate_room_positions(plan)
        optimal_rotation = self._find_optimal_rotation(room_positions)

        print(f"   Optimal rotation: {optimal_rotation:.1f}°")

        vastu_plan = self._rotate_plan(vastu_plan, optimal_rotation)

        final_positions = self._calculate_room_positions(vastu_plan)
        compliance_score = self._calculate_vastu_score(final_positions)

        print(f"   Vastu compliance score: {compliance_score:.1f}%")

        vastu_plan['vastu_applied'] = True
        vastu_plan['vastu_rotation'] = optimal_rotation
        vastu_plan['vastu_score'] = compliance_score
        vastu_plan['vastu_analysis'] = self._generate_vastu_report(final_positions)

        return vastu_plan

    def _calculate_room_positions(self, plan):
        positions = {}
        inner_geom = plan.get('inner')
        if inner_geom and not inner_geom.is_empty:
            plan_center = inner_geom.centroid
        else:
            plan_center = Point(128, 128)

        for room_type in ['kitchen', 'bedroom', 'living', 'bathroom',
                          'front_door', 'balcony']:
            room_geom = plan.get(room_type)

            if room_geom and not room_geom.is_empty:
                room_center = centroid(room_geom)
                dx = room_center.x - plan_center.x
                dy = room_center.y - plan_center.y
                angle = np.degrees(np.arctan2(dx, dy)) % 360
                distance = np.sqrt(dx**2 + dy**2)

                positions[room_type] = {
                    'center': room_center,
                    'angle': angle,
                    'distance': distance,
                    'zone': self._get_zone_for_angle(angle)
                }

        return positions

    def _get_zone_for_angle(self, angle):
        for zone_name, (start, end) in self.zones.items():
            if start <= angle < end or (start > end and (angle >= start or angle < end)):
                return zone_name
        return 'north'

    def _find_optimal_rotation(self, room_positions):
        best_rotation = 0
        best_score = 0

        for rotation in range(0, 360, 45):
            rotated_positions = {}
            for room_type, pos in room_positions.items():
                new_angle = (pos['angle'] + rotation) % 360
                rotated_positions[room_type] = {
                    **pos,
                    'angle': new_angle,
                    'zone': self._get_zone_for_angle(new_angle)
                }

            score = self._calculate_vastu_score(rotated_positions)

            if score > best_score:
                best_score = score
                best_rotation = rotation

        return best_rotation

    def _calculate_vastu_score(self, room_positions):
        total_score = 0
        total_weight = 0

        weights = {
            'kitchen': 1.5,
            'bedroom': 1.3,
            'living': 1.2,
            'bathroom': 1.0,
            'front_door': 1.5,
            'balcony': 0.8,
        }

        for room_type, position in room_positions.items():
            if room_type in self.ideal_placements:
                weight = weights.get(room_type, 1.0)
                current_zone = position['zone']
                ideal_zones = self.ideal_placements[room_type]

                if current_zone in ideal_zones:
                    room_score = 100
                else:
                    room_score = 50

                total_score += room_score * weight
                total_weight += weight

        return (total_score / total_weight) if total_weight > 0 else 50

    def _rotate_plan(self, plan, angle):
        canvas_size = 256
        center_point = (canvas_size / 2, canvas_size / 2)

        for key in ['living', 'bedroom', 'bathroom', 'kitchen',
                    'door', 'window', 'wall', 'front_door', 'balcony',
                    'inner', 'land']:
            geom = plan.get(key)
            if geom and not geom.is_empty:
                plan[key] = affinity.rotate(geom, angle, origin=center_point)

        return plan

    def _generate_vastu_report(self, room_positions):
        report = []
        for room_type, position in room_positions.items():
            if room_type in self.ideal_placements:
                current_zone = position['zone']
                ideal_zones = self.ideal_placements[room_type]
                zone_name = current_zone.replace('_', ' ').title()

                if current_zone in ideal_zones:
                    status = "✅ Optimal"
                else:
                    status = "⚠️ Acceptable"

                report.append(f"**{room_type.title()}**: {zone_name} - {status}")

        return "\n".join(report)


# ============================================================
# FLOOR PLAN GENERATOR
# ============================================================

class FloorPlanGenerator:
    def __init__(self, database):
        self.db = database
        self.vastu = VastuCompliance()
        self.current_plan = None
        self.current_plan_idx = None

    def generate_plan(self, bedrooms, bathrooms, min_area, max_area,
                     has_kitchen, apply_vastu):

        results = self.db.search_plans(
            bedrooms=bedrooms if bedrooms > 0 else None,
            bathrooms=bathrooms if bathrooms > 0 else None,
            min_area=min_area if min_area > 0 else None,
            max_area=max_area if max_area > 0 else None,
            has_kitchen=has_kitchen,
            limit=1
        )

        if not results:
            return None, "❌ No matching floor plans found. Try adjusting your criteria."

        self.current_plan_idx, self.current_plan, score = results[0]

        if apply_vastu:
            self.current_plan = self.vastu.apply_vastu(self.current_plan)

        fig = self._plot_plan(self.current_plan, apply_vastu)
        info = self._get_plan_info(self.current_plan)

        return fig, info

    def _plot_plan(self, plan, vastu_applied=False):
        title = f"Floor Plan (Area: {plan['area']:.2f} sq units)"
        if vastu_applied:
            title += " - Vastu Compliant ✓"

        fig, ax = plt.subplots(figsize=(10, 10))
        ax = plot_plan(plan, ax=ax, title=title, legend=True)
        plt.tight_layout()

        return fig

    def _get_plan_info(self, plan):
        def count_rooms(geom):
            if geom is None or geom.is_empty:
                return 0
            if hasattr(geom, 'geoms'):
                return len(geom.geoms)
            return 1

        bedroom_count = count_rooms(plan.get('bedroom'))
        bathroom_count = count_rooms(plan.get('bathroom'))

        info = f"""
📐 **Floor Plan Details:**
- **Total Area:** {plan['area']:.2f} square units
- **Bedrooms:** {bedroom_count}
- **Bathrooms:** {bathroom_count}
- **Kitchen:** {'Yes' if plan.get('kitchen') and not plan['kitchen'].is_empty else 'No'}
- **Living Room:** {'Yes' if plan.get('living') and not plan['living'].is_empty else 'No'}
- **Balcony:** {'Yes' if plan.get('balcony') and not plan['balcony'].is_empty else 'No'}
        """

        if plan.get('vastu_applied'):
            info += f"""
---
### 🕉️ Vastu Analysis:
**Compliance Score:** {plan['vastu_score']:.1f}%
**Rotation Applied:** {plan['vastu_rotation']:.1f}°
{plan['vastu_analysis']}
            """

        return info


# ============================================================
# GRADIO INTERFACE
# ============================================================

def create_interface(generator):
    with gr.Blocks(title="AI Floor Plan Generator") as demo:
        gr.Markdown("""
        # 🏠 AI Floor Plan Generator with Vastu Shastra
        
        Generate custom 2D floor plans based on your requirements with optional Vastu compliance.
        """)

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📝 Input Your Requirements")

                bedrooms = gr.Slider(0, 6, value=2, step=1, label="Bedrooms (0=any)")
                bathrooms = gr.Slider(0, 4, value=2, step=1, label="Bathrooms (0=any)")

                with gr.Row():
                    min_area = gr.Number(value=80, label="Min Area (sq units)")
                    max_area = gr.Number(value=150, label="Max Area (sq units)")

                has_kitchen = gr.Checkbox(value=True, label="Include Kitchen")
                apply_vastu = gr.Checkbox(value=False, label="🕉️ Apply Vastu Shastra Principles")

                generate_btn = gr.Button("🎨 Generate Floor Plan", variant="primary")

            with gr.Column(scale=2):
                gr.Markdown("### 🖼️ Generated Floor Plan")
                plan_output = gr.Plot(label="2D Floor Plan")

                with gr.Accordion("📊 Plan Information", open=True):
                    plan_info = gr.Markdown("*Generate a plan to see details*")

        generate_btn.click(
            fn=generator.generate_plan,
            inputs=[bedrooms, bathrooms, min_area, max_area, has_kitchen, apply_vastu],
            outputs=[plan_output, plan_info]
        )
        
        gr.Markdown("""
        ---
        ### 📖 About
        This application generates 2D floor plans from a curated database based on your specifications.
        The Vastu Shastra option applies ancient Indian architectural principles for optimal room placement.
        """)

    return demo


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("Initializing Floor Plan Generator...")
    
    # Look for the dataset file
    pkl_path = "ResPlan.pkl"
    if not os.path.exists(pkl_path):
        print("ERROR: ResPlan.pkl not found!")
        print("Please upload your ResPlan.pkl file to the Space.")
        exit(1)
    
    db = FloorPlanDatabase(pkl_path)
    generator = FloorPlanGenerator(db)

    print("\nLaunching Gradio Interface...")
    demo = create_interface(generator)
    demo.launch()