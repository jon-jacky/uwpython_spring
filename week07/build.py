"""
build.py
from http://en.wikibooks.org/wiki/Python_Programming/Extending_with_C

python setup.py build

"""
from distutils.core import setup, Extension

module1 = Extension('hello', sources = ['hellomodule.c'])

setup (name = 'PackageName',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [module1])
