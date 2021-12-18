import sys
from lib import timed_run
import re
import math
from itertools import product


@timed_run
def read_input():
    match = re.match(r'.*x=(-?[0-9]+)\.\.(-?[0-9]+), y=(-?[0-9]+)\.\.(-?[0-9]+)', sys.stdin.read().strip())
    nums = tuple(int(x) for x in match.group(1, 2, 3, 4))
    return nums[:2], nums[2:]


def arithmetic_sum(start, ticks, increment):
    if ticks == 0:
        return 0
    end = start + (ticks - 1) * increment
    return ticks * (start + end) // 2


def calculate_x(velocity, ticks):
    if ticks > velocity:  # velocity stops decreasing at 0
        ticks = velocity
    return arithmetic_sum(velocity, ticks, -1)


def calculate_y(velocity, ticks):
    return arithmetic_sum(velocity, ticks, -1)


def calculate_starting_velocity(target, ticks):
    return target / ticks + (ticks - 1) / 2


def get_valid_range(target, ticks):
    if ticks == 1:
        return target
    min_v, max_v = math.ceil(calculate_starting_velocity(target[0], ticks)), \
        math.floor(calculate_starting_velocity(target[1], ticks))

    return min_v, max_v


def inclusive_range(start, stop):
    yield from range(start, stop)
    yield stop


@timed_run
def solve(x_target, y_target):
    pairs = set()

    # x and y are linked
    prev_x_range, prev_y_range = None, None
    ticks = 1
    while True:
        this_x_range, this_y_range = get_valid_range(x_target, ticks), get_valid_range(y_target, ticks)
        if this_x_range == prev_x_range:
            break
        pairs.update(product(inclusive_range(*this_x_range), inclusive_range(*this_y_range)))
        prev_x_range, prev_y_range = this_x_range, this_y_range
        ticks += 1

    # x no longer changes
    while True:
        this_y_range = get_valid_range(y_target, ticks)
        if this_y_range[0] > 0:
            break
        pairs.update(product(inclusive_range(*this_x_range), inclusive_range(*this_y_range)))
        ticks += 1

    # starting to launch up
    ticks = 1
    while True:
        this_y_range = get_valid_range(y_target, ticks)
        this_y_range = -this_y_range[1] - 1, -this_y_range[0] - 1
        if this_y_range[0] < 0 :
            break
        pairs.update(product(inclusive_range(*this_x_range), inclusive_range(*this_y_range)))
        ticks += 1

    return len(pairs)


if __name__ == '__main__':
    print(solve(*read_input()))
