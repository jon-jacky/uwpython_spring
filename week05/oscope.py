"""
Threads demo: ascii oscilloscope
"""

import threading
import string
import time

class signal(threading.Thread):
    """Signal generator: compute signal, store in circular buffer
    """
    def __init__(self, buflen, interval, period, ncycles):
        threading.Thread.__init__(self)
        self.buffer = list(buflen*'0') # circular buffer
        self.bound = 0 # index past the most recent element in circular buffer
        self.interval = interval # signal sampling interval in sec
        self.period = period  # number of samples in one cycle
        self.ncycles = ncycles # number of cycles to generate before exit

    def run(self):
        """Generate ncycles of sawtooth wave, write into circular buffer
        """
        for icycle in range(self.ncycles):
            for d in string.digits:
                for k in range(self.period/len(string.digits)): # integer division
                    time.sleep(self.interval) 
                    self.buffer[self.bound] = d
                    self.bound = \
                        self.bound + 1 if self.bound < len(self.buffer)-1 else 0

class oscope(threading.Thread):
    """Oscilloscope: periodically display contents of circular buffer
    """
    def __init__(self, signal, linelen, sweep, nsweeps):
        threading.Thread.__init__(self)
        self.signal = signal # signal generator object including buffer
        self.linelen = linelen # length of scope trace dispay in characters
        self.sweep = sweep # sweep interval in sec
        self.nsweeps = nsweeps # number of sweeps to display before exit

    def run(self):
        """Periodically display contents of circular buffer
        """
        s = self.signal
        for i in range(self.nsweeps):
            time.sleep(self.sweep)
            # older samples are at the end of the buffer, above the bound
            print (''.join(s.buffer[s.bound:] + s.buffer[:s.bound]))[:self.linelen]
            print

if __name__ == '__main__':
    sig = signal(100, 0.01, 50, 20)
    scope = oscope(sig, 75, 1.0, 10)
    sig.start()
    scope.start()



        
    
