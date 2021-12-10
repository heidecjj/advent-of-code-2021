import sys
from lib import timed_run


@timed_run
def read_input():
    lines = list()
    for line in sys.stdin:
        lines.append(line.strip())
    return lines


open_to_close = {'(': ')', '[': ']', '{': '}', '<': '>'}
error_point_map = {')': 1, ']': 2, '}': 3, '>': 4}


@timed_run
def solve(lines):
    points = list()
    for line in lines:
        this_points = calculate_error_points(line)
        if this_points:
            points.append(this_points)
    return sorted(points)[len(points) // 2]


def calculate_error_points(line):
    closer_stack = list()
    for char in line:
        try:
            closer_stack.append(open_to_close[char])
        except KeyError:
            expected = closer_stack.pop()
            if char != expected:
                return 0

    if not closer_stack:
        return 0

    points = 0
    for char in reversed(closer_stack):
        points = points * 5 + error_point_map[char]

    return points


if __name__ == '__main__':
    print(solve(read_input()))
