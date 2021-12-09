import sys
from lib import timed_run
from functools import reduce


@timed_run
def read_input():
    heights = list()
    for line in sys.stdin:
        heights.append(tuple(int(point) for point in line.strip()))
    return heights


def expand_basin(row, col, heights):
    seen = set()
    to_expand = {(row, col)}
    max_r = len(heights) - 1
    max_c = len(heights[0]) - 1

    while to_expand:
        r, c = point = to_expand.pop()
        seen.add(point)

        adjacent = ((r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c))
        for new_point in adjacent:
            new_r, new_c = new_point
            if new_point in seen \
                    or new_r < 0 or new_r > max_r or new_c < 0 or new_c > max_c \
                    or heights[new_r][new_c] == 9:
                continue
            to_expand.add(new_point)

    return seen


@timed_run
def solve(heights):
    to_inspect = {(r, c) for r in range(len(heights)) for c in range(len(heights[0])) if heights[r][c] != 9}
    basin_sizes = list()

    while to_inspect:
        r, c = next(iter(to_inspect))
        basin_points = expand_basin(r, c, heights)
        basin_sizes.append(len(basin_points))
        to_inspect -= basin_points

    return reduce(lambda x, y: x * y, sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    print(solve(read_input()))
