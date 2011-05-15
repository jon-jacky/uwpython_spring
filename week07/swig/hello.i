/*
hello.i
from http://en.wikibooks.org/wiki/Python_Programming/Extending_with_C
*/
 
%module hello
extern void say_hello(const char* name);
