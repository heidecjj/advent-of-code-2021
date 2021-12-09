import sys
from lib import timed_run


@timed_run
def read_input():
    heights = list()
    for line in sys.stdin:
        heights.append(tuple(int(point) for point in line.strip()))
    return heights


def is_local_min(value, row, col, heights):
    adjacent = ((row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col))
    return all(value < heights[r][c] for r, c in adjacent if -1 < r < len(heights) and -1 < c < len(heights[0]))


@timed_run
def solve(heights):
    total = 0
    for r_idx, row in enumerate(heights):
        for c_idx, value in enumerate(row):
            if is_local_min(value, r_idx, c_idx, heights):
                total += value + 1
    return total


if __name__ == '__main__':
    print(solve(read_input()))
