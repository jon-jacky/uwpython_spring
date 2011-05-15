"""
setup_integrate.py based on Behnel, Bradshaw, Seljebotn, Cython tutorial
http://conference.scipy.org/proceedings/SciPy2009/paper_1/

python setup_integrate.py build_ext --inplace
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[
    Extension("integratex",      # x suffix 
              ["integrate.pyx"],
              libraries=["m"]) # Unix-like specific
]

setup(
    name = "Demos",
    cmdclass = {"build_ext": build_ext},
    ext_modules = ext_modules
)
