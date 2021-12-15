import sys
from lib import timed_run
from collections import defaultdict
from functools import lru_cache
from copy import copy


@timed_run
def read_input():
    polymer = sys.stdin.readline().strip()
    sys.stdin.readline()
    rules = {left: right for left, right in (line.strip().split(' -> ') for line in sys.stdin)}
    return polymer, rules


def accumulate_counts(one, two):
    for k, v in two.items():
        one[k] += v


def get_counter(rules):
    @lru_cache(None)
    def counter(pair, levels):
        if levels == 0:
            return defaultdict(int)
        new_guy = rules[pair]
        counts = copy(counter(pair[0] + new_guy, levels - 1))
        accumulate_counts(counts, counter(new_guy + pair[1], levels - 1))
        counts[new_guy] += 1
        return counts
    return counter


def get_letter_counter(rules, letter):
    @lru_cache(None)
    def letter_counter(pair, levels):
        if levels == 0:
            return 0
        new_guy = rules[pair]
        l, r = pair
        return int(new_guy == letter) + letter_counter(l + new_guy, levels - 1) + letter_counter(new_guy + r, levels - 1)
    return letter_counter


@timed_run
def cheating(polymer, rules, iterations):
    counter = get_letter_counter(rules, 'H')
    least = polymer.count('H')
    for l, r in zip(polymer[:-1], polymer[1:]):
        least += counter(l + r, iterations)

    counter = get_letter_counter(rules, 'O')
    most = polymer.count('O')
    for l, r in zip(polymer[:-1], polymer[1:]):
        most += counter(l + r, iterations)

    return most - least


@timed_run
def solve(polymer, rules):
    iterations = 40

    counts = defaultdict(int)
    counter = get_counter(rules)

    for c in polymer:
        counts[c] += 1

    for l, r in zip(polymer[:-1], polymer[1:]):
        accumulate_counts(counts, counter(l + r, iterations))
    sorted_counts = sorted(counts.values())

    return sorted_counts[-1] - sorted_counts[0]


if __name__ == '__main__':
    p, r = read_input()
    print(solve(p, r))
    print(cheating(p, r, 40))
