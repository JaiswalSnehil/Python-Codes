import numpy as np
import plotly.express as px

freq = np.linspace(0, 1000, 400)
amp = np.exp(-freq/300) * np.sin(freq/20)

px.line(x=freq, y=amp, title="🎼 Frequency Landscape",
        template="plotly_dark"
).show()