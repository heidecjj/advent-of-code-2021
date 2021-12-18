import sys
from lib import timed_run
import re


@timed_run
def read_input():
    match = re.match(r'.*x=(-?[0-9]+)\.\.(-?[0-9]+), y=(-?[0-9]+)\.\.(-?[0-9]+)', sys.stdin.read().strip())
    nums = tuple(int(x) for x in match.group(1, 2, 3, 4))
    return nums[:2], nums[2:]


@timed_run
def solve(x_range, y_range):
    lowest_y = min(y_range)
    initial_velocity = -lowest_y - 1
    return (initial_velocity * (initial_velocity + 1)) // 2  # max height


if __name__ == '__main__':
    print(solve(*read_input()))
