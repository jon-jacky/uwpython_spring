# SWIG demo
# from http://en.wikibooks.org/wiki/Python_Programming/Extending_with_C
#
# start with hellomodule.c and hello.i
# swig command generates hello.py and hello_wrap.c
# first gcc command compiles, generates hellomodule.o hello_wrap.o
# second gcc command links, generates _hello.so
#
# Then in python
# >>> import hello
# >>> hello.say_hello('World')
# Hello World!

swig -python hello.i 
gcc -fpic -c hellomodule.c hello_wrap.c -I/usr/include/python2.6/
gcc -shared hellomodule.o hello_wrap.o -o _hello.so
