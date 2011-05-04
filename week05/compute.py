"""
Compute-bound program - informative to view CPU activity on System Monitor during run
python compute.py 30000000 (thirty million) takes ~7 sec on 2GHZ Intel Core 2 Duo
"""
import sys

def compute(n):
    result = sum(2*i for i in xrange(n)) # generator expression with xrange
    print 'n: %s, result: %s' % (n, result)
    return n, result

if __name__ == '__main__':
    n = 1000000
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            pass
    compute(n)
