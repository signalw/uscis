"""
This script sorts the output of check_status.py,
assuming the output is stored in a file.

Usage:
    $ python sort_log.py output1.log output2.log
"""

import sys

def sort_log(f_name):
    with open(f_name, "r+") as f:
        cases = sorted([c.strip().split(' ', 1) for c in f.readlines()])
        f.seek(0)
        f.write('\n'.join([' '.join(c) for c in cases]))
        f.truncate()

if __name__ == '__main__':
    for f in sys.argv[1:]:
        sort_log(f)
