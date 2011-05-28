# A very simple setup script to create an executable with a library file.
# (based on the example scripts which ship with py2exe)


from distutils.core import setup
import py2exe

setup(
    zipfile = "lib/library.zip",
    console = ['hello.py', 'environment.py'],
    )
