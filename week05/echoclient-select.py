#!/usr/bin/env python

"""
Based on Daniel Zappala's http://ilab.cs.byu.edu/python/code/echoclientselect.py
Add print statements to show what's going on

An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import socket
import sys

host = 'localhost'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print 'Client connected to', s.getpeername(),
print 'Type return at the % prompt to exit.'
sys.stdout.write('%')

while 1:
    # read from keyboard
    line = sys.stdin.readline()
    if line == '\n':
        break
    s.send(line)
    data = s.recv(size)
    sys.stdout.write(data)
    sys.stdout.write('%')
s.close()
