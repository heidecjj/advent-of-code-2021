import sys
from lib import timed_run


@timed_run
def read_input():
    lines = list()
    for line in sys.stdin:
        lines.append(line.strip())
    return lines


open_to_close = {'(': ')', '[': ']', '{': '}', '<': '>'}
error_point_map = {')': 3, ']': 57, '}': 1197, '>': 25137}


@timed_run
def solve(lines):
    return sum(calculate_error_points(line) for line in lines)


def calculate_error_points(line):
    closer_stack = list()
    for char in line:
        try:
            closer_stack.append(open_to_close[char])
        except KeyError:
            expected = closer_stack.pop()
            if char != expected:
                return error_point_map[char]

    return 0


if __name__ == '__main__':
    print(solve(read_input()))
