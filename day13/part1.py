import sys
from lib import timed_run


@timed_run
def read_input():
    dots = set()
    folds = list()
    reading_dots = True
    for line in sys.stdin:
        if not line.strip():
            reading_dots = False
            continue
        if reading_dots:
            dots.add(tuple(int(x) for x in line.strip().split(',')))
        else:
            direction, value = line.strip().split()[-1].split('=')
            folds.append((direction, int(value)))
    return dots, folds


def horizontal_fold(dot, line_value):
    x, y = dot
    if y <= line_value:
        return dot
    return x,  line_value - (y - line_value)


def vertical_fold(dot, line_value):
    x, y = dot
    if x <= line_value:
        return dot
    return line_value - (x - line_value),  y


def fold(dots, direction, line_value):
    transform = vertical_fold if direction == 'x' else horizontal_fold
    return {transform(dot, line_value) for dot in dots}


@timed_run
def solve(dots, folds):
    direction, value = folds[0]
    return len(fold(dots, direction, value))


if __name__ == '__main__':
    print(solve(*read_input()))
