from vpython import *

sphere(radius=2, texture=textures.earth)
sat = box(pos=vector(5,0,0), size=0.5, color=color.white)

a = 0
while True:
    rate(60)
    a =+ 0.02
    sat.pos = vector(5*cos(a), 0, 5*sin(a))