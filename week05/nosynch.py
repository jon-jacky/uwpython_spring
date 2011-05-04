"""
Threads demo - no synchronization
"""

import threading 

class CharPrinter(threading.Thread):
    """A thread class is a subclass of threading.Thread
    """
    def __init__(self, ch, nreps):
        """A thread class __init__ must call the base class __init__
        """
        threading.Thread.__init__(self)
        self.ch = ch
        self.nreps = nreps

    def run(self):
        """ A thread class must have a run method
        """
        for i in range(self.nreps):
            print self.ch,

if __name__ == '__main__':
    # create some threads
    c1 = CharPrinter('X', 100)
    c2 = CharPrinter('0', 100)

    # start each thread
    c1.start()
    c2.start()

