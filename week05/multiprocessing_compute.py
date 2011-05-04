"""
Compute-bound processes - view CPU activity on System Monitor during run
"""

from multiprocessing import Process
from compute import compute

if __name__ == '__main__':
    p1 = Process(target=compute, args=(30000000,))
    p2 = Process(target=compute, args=(30000001,))
    p1.start()
    p2.start() # comment out this line to see effect of just one running process



