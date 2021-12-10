import sys
from lib import timed_run


@timed_run
def read_input():
    lines = list()
    for line in sys.stdin:
        lines.append(line)
    return lines


@timed_run
def solve(lines):
    return lines


if __name__ == '__main__':
    print(solve(read_input()))
