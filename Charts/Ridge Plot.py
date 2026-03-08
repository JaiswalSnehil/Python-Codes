import numpy as np
import plotly.graph_objects as go

np.random.seed(42)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# Fixed color codes
colors = ['#A3B18A', '#588157', '#3A5A40', '#BC6C25', '#DDA15E']

fig = go.Figure()

for i, month in enumerate(months):
    data = np.random.normal(loc=i*5, scale=2, size=200)
    
    fig.add_trace(go.Violin(
        x=data,
        y=[month]*len(data),
        orientation='h',
        line_color=colors[i],
        fillcolor=colors[i],
        opacity=0.6,
        showlegend=False
    ))

fig.update_layout(
    title='Sales Distribution by Month (Ridge Plot)',
    paper_bgcolor='#FAF9F6',
    plot_bgcolor='#FAF9F6',
    font_family='serif',
    width=900,
    height=500
)

fig.show()