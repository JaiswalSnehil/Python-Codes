from sympy import *

x = symbols('x')
expr = (cos(x)**2 * sqrt(1-x**2) + sin(x**3))**-1/ \
    log(1 + sin(2*x*sqrt(1-x**2))/pi + exp(x)/(1+x**2)) \
    + tan(x)/(1 + sqrt(1+x**4))

pprint(Integral(expr, x))