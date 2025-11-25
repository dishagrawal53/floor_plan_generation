<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Floor Plan Generator with Vastu Shastra</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #ffffff;
        }
        h1 {
            border-bottom: 3px solid #0366d6;
            padding-bottom: 10px;
            color: #0366d6;
        }
        h2 {
            border-bottom: 2px solid #e1e4e8;
            padding-bottom: 8px;
            margin-top: 30px;
            color: #24292e;
        }
        h3 {
            color: #0366d6;
            margin-top: 20px;
        }
        .badge {
            display: inline-block;
            padding: 4px 8px;
            margin: 2px;
            border-radius: 3px;
            font-size: 12px;
            font-weight: 600;
        }
        .badge-python {
            background: #3776ab;
            color: white;
        }
        .badge-gradio {
            background: #ffd4a3;
            color: #333;
        }
        .badge-vastu {
            background: #ffe4b3;
            color: #333;
        }
        .badge-colab {
            background: #fff9b3;
            color: #333;
        }
        .badge-huggingface {
            background: #ffc9d4;
            color: #333;
        }
        code {
            background: #f6f8fa;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
        }
        pre {
            background: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            border: 1px solid #e1e4e8;
        }
        pre code {
            background: none;
            padding: 0;
        }
        .demo-box {
            background: #fef5e7;
            color: #333;
            padding: 25px;
            border-radius: 8px;
            text-align: center;
            margin: 25px 0;
            border: 2px solid #f9e79f;
        }
        .demo-box a {
            color: #e67e22;
            font-size: 18px;
            font-weight: 600;
            text-decoration: none;
            background: white;
            border: 2px solid #e67e22;
            padding: 12px 24px;
            border-radius: 6px;
            display: inline-block;
            margin-top: 12px;
            transition: all 0.3s ease;
        }
        .demo-box a:hover {
            background: #e67e22;
            color: white;
        }
        .highlight {
            background: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ffc107;
            margin: 15px 0;
        }
        .credit-box {
            background: #e7f3ff;
            padding: 15px;
            border-left: 4px solid #0366d6;
            margin: 15px 0;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .feature-card {
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 15px;
            background: #f6f8fa;
        }
        .feature-card h4 {
            margin-top: 0;
            color: #0366d6;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #e1e4e8;
            padding: 10px;
            text-align: left;
        }
        th {
            background: #f6f8fa;
            font-weight: 600;
        }
        .emoji {
            font-size: 1.2em;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .file-structure {
            background: #f6f8fa;
            padding: 15px;
            border-radius: 6px;
            border: 1px solid #e1e4e8;
            font-family: 'Courier New', monospace;
            font-size: 14px;
        }
        .component-box {
            border: 2px solid #0366d6;
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            background: #f8f9fa;
        }
        .component-box h3 {
            margin-top: 0;
            color: #0366d6;
        }
    </style>
</head>
<body>

<h1><span class="emoji">🏠</span> AI Floor Plan Generator with Vastu Shastra</h1>

<p>
    <span class="badge badge-python">Python 3.8+</span>
    <span class="badge badge-gradio">Gradio</span>
    <span class="badge badge-vastu">Vastu Compliant</span>
    <span class="badge badge-colab">Google Colab</span>
    <span class="badge badge-huggingface">Hugging Face</span>
</p>

<div class="demo-box">
    <h2 style="margin-top: 0;">Try the Live Demo</h2>
    <p>Experience the floor plan generator in action</p>
    <a href="https://huggingface.co/spaces/itsmedi/floor_plan_generator" target="_blank">
        Launch Demo
    </a>
</div>

<h2><span class="emoji">📖</span> Overview</h2>

<p>
This floor plan generation system creates customized 2D residential layouts based on your specific requirements. 
Built on the ResPlan dataset of 17,107 floor plans, it can apply traditional Vastu Shastra 
principles to align your space with ancient architectural wisdom.
</p>

<p>The repository includes:</p>

<ul>
    <li><strong>app.py</strong> - Web application with interactive interface (live on Hugging Face)</li>
    <li><strong>floor_plan_gen.ipynb</strong> - Research notebook for exploration and testing (works on Google Colab)</li>
</ul>

<h2><span class="emoji">🎯</span> Repository Components</h2>

<div class="component-box">
    <h3><span class="emoji">🌐</span> app.py - Web Application</h3>
    <p><strong>What it does:</strong> A ready-to-use web interface where you can generate floor plans through your browser</p>
    <p><strong>Features:</strong></p>
    <ul>
        <li>Easy-to-use interface with sliders and checkboxes</li>
        <li>Generates floor plans in real-time</li>
        <li>Toggle Vastu Shastra compliance on/off</li>
        <li>Clear 2D visualization with labeled rooms</li>
        <li>Shows detailed information about each plan</li>
    </ul>
    <p><strong>Where to find it:</strong> Running live at 
    <a href="https://huggingface.co/spaces/itsmedi/floor_plan_generator" target="_blank">itsmedi/floor_plan_generator</a></p>
</div>

<div class="component-box">
    <h3><span class="emoji">📓</span> floor_plan_gen.ipynb - Research Notebook</h3>
    <p><strong>What it does:</strong> A notebook for experimenting with the dataset and testing different approaches</p>
    <p><strong>Features:</strong></p>
    <ul>
        <li>Explore the full dataset of 17,107 floor plans</li>
        <li>Test geometric transformations (rotate, flip, scale)</li>
        <li>Experiment with buffer operations for cleaning geometries</li>
        <li>Analyze room connectivity through graphs</li>
        <li>Test and refine Vastu compliance algorithms</li>
        <li>Create custom visualizations</li>
    </ul>
    <p><strong>Best for:</strong> Google Colab with Google Drive integration</p>
    
    <p><strong>What's inside:</strong></p>
    <ol>
        <li>Loading the dataset from Google Drive</li>
        <li>Exploring floor plan statistics</li>
        <li>Testing geometric transformations</li>
        <li>Cleaning geometries with buffer operations</li>
        <li>Building and analyzing connectivity graphs</li>
        <li>Implementing Vastu principles</li>
        <li>Creating professional visualizations</li>
    </ol>
</div>

<h2><span class="emoji">✨</span> Features</h2>

<div class="feature-grid">
    <div class="feature-card">
        <h4><span class="emoji">🔍</span> Intelligent Search</h4>
        <p>Index-based filtering by bedrooms, bathrooms, area range, and kitchen presence</p>
    </div>
    <div class="feature-card">
        <h4><span class="emoji">🕉️</span> Vastu Shastra</h4>
        <p>Automatic orientation optimization based on ancient Indian architectural principles with scoring</p>
    </div>
    <div class="feature-card">
        <h4><span class="emoji">🎨</span> Professional Visualization</h4>
        <p>High-quality 2D floor plans with color-coded rooms, icons, dimensions, and labels</p>
    </div>
    <div class="feature-card">
        <h4><span class="emoji">📊</span> Graph Analysis</h4>
        <p>Room connectivity graphs showing spatial relationships and adjacency</p>
    </div>
</div>



<h2><span class="emoji">📊</span> Dataset Information</h2>

<table>
    <tr>
        <th>Metric</th>
        <th>Value</th>
    </tr>
    <tr>
        <td><strong>Total Floor Plans</strong></td>
        <td>17,107</td>
    </tr>
    <tr>
        <td><strong>Bedroom Range</strong></td>
        <td>0-6 bedrooms</td>
    </tr>
    <tr>
        <td><strong>Bathroom Range</strong></td>
        <td>1-4 bathrooms</td>
    </tr>
    <tr>
        <td><strong>Area Range</strong></td>
        <td>0.09 - 712.94 square units</td>
    </tr>
    <tr>
        <td><strong>Plans with Kitchen</strong></td>
        <td>99.5%</td>
    </tr>
    <tr>
        <td><strong>Data Format</strong></td>
        <td>Vector-based geometry (Shapely)</td>
    </tr>
</table>





<h2><span class="emoji">💡</span> How It Works</h2>

<h3>Finding the Right Floor Plan</h3>
<p>The system uses smart indexing to quickly search through thousands of floor plans:</p>
<ul>
    <li><strong>Bedroom Index:</strong> Organized by number of bedrooms for instant filtering</li>
    <li><strong>Bathroom Index:</strong> Grouped by bathroom count</li>
    <li><strong>Area Index:</strong> Sorted by size for range searches</li>
</ul>

<h3>Applying Vastu Principles</h3>
<p>When you enable Vastu optimization, here's what happens:</p>
<ul>
    <li>The system identifies where each room is located</li>
    <li>Calculates which direction each room faces (North, East, South, West, and corners)</li>
    <li>Tests different rotations of the entire floor plan</li>
    <li>Scores each rotation based on how well rooms align with traditional guidelines</li>
    <li>Applies the best rotation to your floor plan</li>
</ul>

<table>
    <tr>
        <th>Direction</th>
        <th>Zone</th>
        <th>Ideal Placement</th>
    </tr>
    <tr>
        <td><strong>North-East</strong></td>
        <td>Ishaan (Water)</td>
        <td>Entrance, Living room, Prayer room</td>
    </tr>
    <tr>
        <td><strong>South-East</strong></td>
        <td>Agni (Fire)</td>
        <td>Kitchen, Electrical appliances</td>
    </tr>
    <tr>
        <td><strong>South-West</strong></td>
        <td>Nairutya (Earth)</td>
        <td>Master bedroom, Heavy storage</td>
    </tr>
    <tr>
        <td><strong>North-West</strong></td>
        <td>Vayavya (Air)</td>
        <td>Guest room, Bathroom</td>
    </tr>
    <tr>
        <td><strong>North</strong></td>
        <td>Kubera (Wealth)</td>
        <td>Living room, Cash/valuables</td>
    </tr>
    <tr>
        <td><strong>East</strong></td>
        <td>Indra (Sun)</td>
        <td>Main entrance (most auspicious)</td>
    </tr>
</table>

<h3>Creating the Visualization</h3>
<p>Floor plans are drawn in layers:</p>
<ol>
    <li><strong>Room Floors:</strong> Each room type gets its own color</li>
    <li><strong>Walls:</strong> Black lines showing boundaries</li>
    <li><strong>Doors:</strong> Brown circles marking entrances</li>
    <li><strong>Windows:</strong> Blue squares for natural light</li>
    <li><strong>Labels:</strong> Room names with icons so you can tell them apart</li>
    <li><strong>Dimensions:</strong> Size measurements where helpful</li>
    <li><strong>Legend:</strong> A key explaining all the colors and symbols</li>
</ol>

<h2><span class="emoji">🎨</span> Example Output</h2>

<p>The system generates floor plans with:</p>

<table>
    <tr>
        <th>Element</th>
        <th>Visual Style</th>
        <th>Color</th>
    </tr>
    <tr>
        <td><span class="emoji">🛋️</span> Living Room</td>
        <td>Filled polygon</td>
        <td>#FFFACD (Lemon Chiffon)</td>
    </tr>
    <tr>
        <td><span class="emoji">🛏️</span> Bedroom</td>
        <td>Filled polygon</td>
        <td>#E6F3E6 (Light Green)</td>
    </tr>
    <tr>
        <td><span class="emoji">🍳</span> Kitchen</td>
        <td>Filled polygon</td>
        <td>#FFE6E6 (Light Pink)</td>
    </tr>
    <tr>
        <td><span class="emoji">🚿</span> Bathroom</td>
        <td>Filled polygon</td>
        <td>#E6F2FF (Light Blue)</td>
    </tr>
    <tr>
        <td><span class="emoji">🌿</span> Balcony</td>
        <td>Filled polygon</td>
        <td>#F5F5DC (Beige)</td>
    </tr>
    <tr>
        <td><span class="emoji">🚪</span> Doors</td>
        <td>Circle marker</td>
        <td>#8B4513 (Brown)</td>
    </tr>
    <tr>
        <td><span class="emoji">🪟</span> Windows</td>
        <td>Rectangle marker</td>
        <td>#4169E1 (Royal Blue)</td>
    </tr>
    <tr>
        <td>Walls</td>
        <td>Thick lines</td>
        <td>#1A1A1A (Near Black)</td>
    </tr>
</table>

<h2><span class="emoji">🔬</span> Advanced Features in Notebook</h2>

<h3>Geometric Augmentation</h3>
<pre><code># Rotate, flip, and scale floor plans
aug_plan = augment_geom(
    plan,
    degree=45,         # Rotation angle
    flip_vertical=True, # Mirror flip
    scale=0.9          # Scale factor
)</code></pre>

<h3>Buffer Operations</h3>
<pre><code># Clean geometry (remove noise)
cleaned = buffer_shrink_expand(plan['living'], wall_width/2)

# Fill gaps (close small openings)
filled = buffer_expand_shrink(plan['living'], wall_width/2)</code></pre>

<h3>Graph Analysis</h3>
<pre><code># Generate room connectivity graph
G = plan_to_graph(plan)
print(f'Nodes: {G.number_of_nodes()}')
print(f'Edges: {G.number_of_edges()}')

# Visualize with graph overlay
plot_plan_and_graph(plan, title='Floor Plan with Connectivity')</code></pre>

<h2><span class="emoji">🙏</span> Credits & Acknowledgments</h2>

<div class="credit-box">
    <h3><span class="emoji">📚</span> Dataset Source</h3>
    <p><strong>ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans</strong></p>
    <p><strong>Authors:</strong> Mohamed Abouagour, Eleftherios Garyfallidis</p>
    <p><strong>Repository:</strong> <a href="https://github.com/m-agour/ResPlan" target="_blank">https://github.com/m-agour/ResPlan</a></p>
    <p><strong>Dataset:</strong> <a href="https://github.com/m-agour/ResPlan/blob/main/ResPlan.zip" target="_blank">Download ResPlan.zip</a></p>
    
    <p><strong>Citation:</strong></p>
    <pre><code>@article{resplan2024,
  title={ResPlan: A Large-Scale Vector-Graph Dataset of Residential Floor Plans},
  author={Abouagour, Mohamed and Garyfallidis, Eleftherios},
  year={2024},
  publisher={GitHub},
  howpublished={\url{https://github.com/m-agour/ResPlan}}
}</code></pre>
</div>

<div class="credit-box">
    <h3><span class="emoji">🏛️</span> Vastu Shastra Knowledge</h3>
    <p>Vastu principles implemented based on traditional Indian architectural guidelines and sacred geometry.</p>
</div>







<h2><span class="emoji">🗺️</span> What's Next</h2>

<ul>
    <li>✅ Basic floor plan generation</li>
    <li>✅ Vastu Shastra compliance</li>
    <li>✅ Web interface</li>
    <li>✅ Room connectivity graphs</li>
    <li>🔄 Working on 3D visualization</li>
    <li>📋 Planning furniture placement</li>
    <li>📋 Cost estimation tools</li>
    <li>📋 Mobile version</li>
</ul>

<hr>


</body>
</html>
