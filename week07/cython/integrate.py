"""
from Behnel, Bradshaw, Seljebotn, Cython tutorial
http://conference.scipy.org/proceedings/SciPy2009/paper_1/
"""

from math import sin

def f(x):
    return sin(x*x)

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
