import sympy as sp
from IPython.display import display

x = sp.symbols('x')
sinc = sp.Piecewise(
    (1, x==0),
    (sp.sin(x)/x, True)
)
display(sp.Eq(sp.Function("sinc")(x), sinc))