# A very simple setup script to create an executable.
# (based on the example scripts which ship with py2exe)


from distutils.core import setup
import py2exe

setup(
    console = ["hello.py"],
    )
