/*
hellomodule.c
from http://en.wikibooks.org/wiki/Python_Programming/Extending_with_C
*/
 
#include <stdio.h>
 
void say_hello(const char* name) {
    printf("Hello %s!\n", name);
}
