import sys
from lib import timed_run
from collections import defaultdict


@timed_run
def read_input():
    polymer = sys.stdin.readline().strip()
    sys.stdin.readline()
    rules = {left: right for left, right in (line.strip().split(' -> ') for line in sys.stdin)}
    return polymer, rules


@timed_run
def solve(polymer, rules):
    for _ in range(10):
        new_polymer = ""
        for l, r in zip(polymer[:-1], polymer[1:]):
            new_polymer += f'{l}{rules[l+r]}'
        polymer = new_polymer + r
    counts = defaultdict(int)
    for char in polymer:
        counts[char] += 1

    sorted_counts = sorted(counts.values())
    return sorted_counts[-1] - sorted_counts[0]


if __name__ == '__main__':
    print(solve(*read_input()))
