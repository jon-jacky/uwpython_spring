import sys
import py2exe_helper

print "Hello from py2exe"
print

print "len(sys.path)   %s" % len(sys.path)
print "sys.path[0]     %s" % sys.path[0]
print "sys.executable  %s" % sys.executable
print "sys.prefix      %s" % sys.prefix
print "sys.argv        %s" % sys.argv
print "sys.frozen      %s" % getattr(sys, "frozen",    
                                        'AttributeError')
print "App directory   %s" % py2exe_helper.get_main_dir()


