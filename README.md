<h1>🏠 AI Floor Plan Generator with Vastu Shastra</h1>

<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gradio-App-FEAA3A?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Vastu-Compliant-FFC107?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Colab-Notebook-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"/>
  <img src="https://img.shields.io/badge/HuggingFace-Space-FCC72C?style=for-the-badge&logo=huggingface"/>
</p>

<hr/>

<h2>🚀 Live Demo</h2>
<p>
  Try the full web app here:<br/>
  <a href="https://huggingface.co/spaces/itsmedi/floor_plan_generator"><b>👉 Launch on Hugging Face</b></a>
</p>

<hr/>

<h2>📖 Overview</h2>
<p>
This system generates <b>custom 2D residential floor plans</b> using the <b>ResPlan dataset (17,107 plans)</b>.
It also applies <b>Vastu Shastra</b> rules to optimize layout and orientation.
</p>

<p>The repository contains:</p>
<ul>
  <li><b>app.py</b> – Gradio-based web app (live on Hugging Face)</li>
  <li><b>floor_plan_gen.ipynb</b> – Google Colab research and analysis notebook</li>
</ul>

<hr/>

<h2>🎯 Repository Components</h2>

<h3>🌐 <code>app.py</code> — Web Application</h3>
<ul>
  <li>Interactive UI with sliders/toggles</li>
  <li>Generates plans in real-time</li>
  <li>Optional Vastu optimization</li>
  <li>Labeled 2D visualizations</li>
</ul>
<p>Live here: <a href="https://huggingface.co/spaces/itsmedi/floor_plan_generator">itsmedi/floor_plan_generator</a></p>

<h3>📓 <code>floor_plan_gen.ipynb</code> — Research Notebook</h3>
<ul>
  <li>Dataset exploration</li>
  <li>Geometric transforms (rotate, flip, scale)</li>
  <li>Buffer operations for cleaning geometry</li>
  <li>Room connectivity graphs</li>
  <li>Vastu scoring & optimization</li>
  <li>Custom visualizations</li>
</ul>

<hr/>

<h2>✨ Features</h2>
<ul>
  <li>🔍 Intelligent Search & Filters</li>
  <li>🕉️ Vastu Shastra-Based Orientation Optimization</li>
  <li>🎨 Professional 2D Visualization</li>
  <li>📊 Graph Analysis of Room Connectivity</li>
</ul>

<hr/>

<h2>📊 Dataset Information</h2>

<table>
  <tr><th>Metric</th><th>Value</th></tr>
  <tr><td>Total Floor Plans</td><td>17,107</td></tr>
  <tr><td>Bedrooms</td><td>0–6</td></tr>
  <tr><td>Bathrooms</td><td>1–4</td></tr>
  <tr><td>Area Range</td><td>0.09–712.94 units</td></tr>
  <tr><td>Kitchens</td><td>99.5%</td></tr>
  <tr><td>Format</td><td>Vector Geometry (Shapely)</td></tr>
</table>

<hr/>

<h2>💡 How It Works</h2>

<h3>1️⃣ Index-Based Search</h3>
<ul>
  <li>Bedroom filtering</li>
  <li>Bathroom filtering</li>
  <li>Area range search</li>
</ul>

<h3>2️⃣ Vastu Optimization</h3>
<ul>
  <li>Detects room directions</li>
  <li>Rotates plan to test all 4 orientations</li>
  <li>Scores each orientation based on Vastu principles</li>
  <li>Applies best-scoring rotation</li>
</ul>

<h3>3️⃣ Visualization Layers</h3>
<ul>
  <li>Room polygons (colored)</li>
  <li>Walls, doors, windows</li>
  <li>Room labels + icons</li>
  <li>Dimensions</li>
  <li>Legend</li>
</ul>

<hr/>

<h2>🎨 Example Output Style</h2>

<table>
  <tr><th>Element</th><th>Style</th><th>Color</th></tr>
  <tr><td>Living Room</td><td>Polygon</td><td>Lemon Chiffon</td></tr>
  <tr><td>Bedroom</td><td>Polygon</td><td>Light Green</td></tr>
  <tr><td>Kitchen</td><td>Polygon</td><td>Light Pink</td></tr>
  <tr><td>Bathroom</td><td>Polygon</td><td>Light Blue</td></tr>
  <tr><td>Balcony</td><td>Polygon</td><td>Beige</td></tr>
  <tr><td>Doors</td><td>Circle</td><td>Brown</td></tr>
  <tr><td>Windows</td><td>Rectangle</td><td>Royal Blue</td></tr>
  <tr><td>Walls</td><td>Thick Lines</td><td>Black</td></tr>
</table>

<hr/>

<h2>🔬 Advanced Notebook Features</h2>

<h3>Geometry Augmentation</h3>
<pre>
<code>
aug_plan = augment_geom(plan, degree=45, flip_vertical=True, scale=0.9)
</code>
</pre>

<h3>Buffer Operations</h3>
<pre>
<code>
cleaned = buffer_shrink_expand(plan['living'], wall_width/2)
filled  = buffer_expand_shrink(plan['living'], wall_width/2)
</code>
</pre>

<h3>Connectivity Graph</h3>
<pre>
<code>
G = plan_to_graph(plan)
print(G.number_of_nodes(), G.number_of_edges())
plot_plan_and_graph(plan)
</code>
</pre>

<hr/>

<h2>🙏 Credits & Acknowledgments</h2>

<h3>📚 ResPlan Dataset</h3>
<p>
<b>ResPlan: A Large-Scale Vector-Graph Dataset of Residential Floor Plans</b><br/>
Authors: Mohamed Abouagour, Eleftherios Garyfallidis<br/>
GitHub: <a href="https://github.com/m-agour/ResPlan">https://github.com/m-agour/ResPlan</a>
</p>

<pre>
<code>
@article{resplan2024,
  title={ResPlan: A Large-Scale Vector-Graph Dataset of Residential Floor Plans},
  author={Abouagour, Mohamed and Garyfallidis, Eleftherios},
  year={2024},
  publisher={GitHub},
  howpublished={\url{https://github.com/m-agour/ResPlan}}
}
</code>
</pre>



