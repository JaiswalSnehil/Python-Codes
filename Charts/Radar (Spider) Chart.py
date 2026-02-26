import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Score': [90, 80, 60, 85, 75, 95, 70, 85, 90, 60, 80, 70],
    'Skill': ['Logic', 'Art', 'Code', 'Math', 'Team', 'Speech'] * 2,
    'Person': ['Expert', 'Expert', 'Expert', 'Expert', 'Expert', 'Expert',
               'Noivce', 'Noivce', 'Noivce', 'Noivce', 'Noivce', 'Noivce']
})
fig = px.line_polar(df, r='Score', theta='Skill', color='Person',
                    line_close=True, template='plotly_dark',
                    color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(fill='toself', opacity=0.6)
fig.show()