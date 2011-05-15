"""
from Behnel, Bradshaw, Seljebotn, Cython tutorial
http://conference.scipy.org/proceedings/SciPy2009/paper_1/
"""

cdef extern from "math.h":
    double sin(double)

cdef double f(double x):
    return sin(x*x)

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
