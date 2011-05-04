"""
Compute-bound threads - informative to view CPU activity on System Monitor during run
"""

import threading
from compute import compute

class compute_thread(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n

    def run(self):
        compute(self.n)


if __name__ == '__main__':
    c1 = compute_thread(30000000)
    c2 = compute_thread(30000001)
    c1.start()
    c2.start() # comment out this line to see effect of just one running thread
