import sys
from collections import namedtuple, defaultdict
from itertools import product


Point = namedtuple('Point', 'x y')
Line = namedtuple('Line', 's e')


def read_input():
    lines = list()
    for raw in sys.stdin:
        left, right = (x.strip() for x in raw.split('->'))

        lines.append(Line(*sorted((Point(*(int(x) for x in left.split(','))),
                                   Point(*(int(x) for x in right.split(',')))))))

    return lines


def is_horizontal(line):
    return line.s.y == line.e.y


def is_vertical(line):
    return line.s.x == line.e.x


def count_intersections(lines):
    point_count = defaultdict(int)  # Point -> number of lines covering it

    for line in lines:
        if is_horizontal(line):
            for x in range(line.s.x, line.e.x + 1):
                point_count[Point(x, line.s.y)] += 1
        elif is_vertical(line):
            for y in range(line.s.y, line.e.y + 1):
                point_count[Point(line.s.x, y)] += 1
        else:
            y_dir = -1 if line.s.y > line.e.y else 1
            for x, y in zip(range(line.s.x, line.e.x + 1), range(line.s.y, line.e.y + y_dir, y_dir)):
                point_count[Point(x, y)] += 1

    return sum(num > 1 for num in point_count.values())


if __name__ == '__main__':
    print(count_intersections(read_input()))
