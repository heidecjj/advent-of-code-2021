import argparse
from functools import lru_cache


@lru_cache
def do_fish(n):
    if n <= 0:
        return 1
    return do_fish(n - 7) + do_fish(n - 9)


parser = argparse.ArgumentParser()
parser.add_argument('iterations', type=int)
parser.add_argument('state')
ns = parser.parse_args()

total = 0
for num in (int(x) for x in ns.state.split(',')):
    total += do_fish(ns.iterations - num)

print(total)
