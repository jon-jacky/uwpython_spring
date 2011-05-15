"""
setup.py from Behnel, Bradshaw, Seljebotn, Cython tutorial
http://conference.scipy.org/proceedings/SciPy2009/paper_1/

python setup.py build_ext --inplace
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("hello", ["hello.pyx"])]

setup(
    name = 'Hello world app',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
