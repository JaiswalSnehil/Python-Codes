import plotly.graph_objects as go

label = ['Inspiration', 'Moodboard', 'Sketch', 'Final EEdit', 'Pinterest','Instagram']
source = [0, 0, 1, 1, 2, 3, 3]
target = [1, 2, 2, 3, 3, 4, 5]
value = [40, 20, 30, 25, 45, 30, 25]

node_colors = ['#E6E2D3', '#DBC1AD', '#A69080', '#C9ADA7', '#9A8C98', '#F2E9E4']
link_colors = "rgba(201, 173, 167,0.3)"

fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 30,
        thickness = 12,
        line = dict(color = 'white', width = 1),
        label = label,
        color = node_colors
    ),
    link = dict(
        source = source,
        target = target,
        value = value,
        color = link_colors
))])

fig.update_layout(
    font_size = 14,
    font_family = 'serif',
    paper_bgcolor = '#FAF9F6',
    plot_bgcolor = '#FAF9F6',
    width = 1000,
    height = 600,
    margin = dict(l=50, r=50, t=50, b=50)
)

fig.show()