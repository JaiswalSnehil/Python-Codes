import pygal
from IPython.display import display, SVG

radar = pygal.Radar()
radar.title = 'Country Comparision'
radar.x_labels = ['GDP','Population','CO2','Internet']
radar.add('USA',[21,331,5000,88])
radar.add('China',[14,1393,10000,65])
radar.add('India',[3,1380,2500,45])

display(SVG(radar.render_in_browser()))