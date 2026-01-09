from skyfield.api import load
import plotly.graph_objects as go

ts = load.timescale()
sat = load.tle_file("https://celestrak.org/NORAD/elements/stations.txt")[0]
times = ts.utc(2026,1,1,range(0,90,5))

xs,ys,zs = [],[],[]
for t in times:
    pos = sat.at(t).position.km
    xs.append(pos[0])
    ys.append(pos[1])
    zs.append(pos[2])

fig = go.Figure(go.Scatter3d(x=xs,y=ys,z=zs,mode='lines'))
fig.update_layout(title="ISS Orbit Around Earth")
fig.show()