import altair as alt
import pandas as pd
import numpy as np
import webbrowser
import tempfile

#alt.renderers.enable('default') 

df = pd.DataFrame(np.random.randn(50, 2), columns=['x', 'y'])

chart = alt.Chart(df).mark_circle(size=100).encode(
    x='x',
    y='y',
    color='y',
    tooltip=['x', 'y']
)

html = chart.to_html()

with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
    f.write(html)
    webbrowser.open('file://' + f.name)