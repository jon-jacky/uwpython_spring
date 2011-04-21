"""
test script for trun.py and clogdiff
 - run test script: trun.py test_ls
 - save test script output: test script output: trun.py test_ls > test_ls.ref
 - rerun test script, compare output to saved output: clogdiff trun.py test_ls
"""

cases = [
    ('Test the command: ls -l',
     'ls -l'),

    ('Test the command: ls -ltr',
     'ls -ltr'),
]
