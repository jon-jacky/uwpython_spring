#!/usr/bin/env python

"""
Based on Daniel Zappala's http://ilab.cs.byu.edu/python/code/echoserver-select.py
Add print statements to show what's going on.
Use SO_REUSEADDR to avoid 'Address already in use' errors
Add timeout

An echo server that uses select to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import select
import socket
import sys
import time
import datetime

host = ''
port = 50000
backlog = 5
size = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host,port))
server.listen(5)
print """Server starting, to exit type RETURN in this window
Listening on port %s""" % port
timeout = 5 # seconds
input = [server,sys.stdin]
running = 1
while running:
    inputready,outputready,exceptready = select.select(input,[],[],timeout)

    # timeout
    if not inputready:  
        print 'Server running at %s' % datetime.datetime.now()

    for s in inputready:

        if s == server:
            # handle the server socket
            client, address = server.accept()
            input.append(client)
            print 'Client connected from', address

        elif s == sys.stdin:
            # handle standard input
            junk = sys.stdin.readline()
            running = 0 
            print 'Input %s from stdin, exiting.' % junk.strip('\n')

        elif s:
            # handle all other sockets
            data = s.recv(size)
            print '%s: %s' % (s.getpeername(), data.strip('\n'))
            if data:
                s.send(data)
            else:
                s.close()
                input.remove(s)

server.close()
