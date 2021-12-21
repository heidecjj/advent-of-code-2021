import sys
from lib import timed_run
from functools import lru_cache
from itertools import product


@timed_run
def read_input():
    lines = list()
    for line in sys.stdin:
        lines.append(int(line.split(': ')[1].strip()))
    return lines

# num worlds - outcome of 3 rolls
die_outcomes = (
    (1, 3),
    (3, 4),
    (6, 5),
    (7, 6),
    (6, 7),
    (3, 8),
    (1, 9),
)
goal = 21


@lru_cache(None)
def count_wins(positions, scores):
    if scores[0] >= goal:
        return 1, 0
    elif scores[1] >= goal:
        return 0, 1

    results = [0, 0]
    for p1 in die_outcomes:
        new_p1_position = add_positions(positions[0], p1[1])
        new_p1_score = scores[0] + new_p1_position
        if new_p1_score >= goal:
            results[0] += p1[0]
            continue
        for p2 in die_outcomes:
            new_p2_position = add_positions(positions[1], p2[1])
            new_p2_score = scores[1] + new_p2_position
            num_universes = p1[0] * p2[0]
            if new_p2_score >= goal:
                results[1] += num_universes
                continue
            counts = count_wins((new_p1_position, new_p2_position), (new_p1_score, new_p2_score))
            results[0] += num_universes * counts[0]
            results[1] += num_universes * counts[1]
    return tuple(results)


def add_positions(pos, add):
    new_position = (pos + add) % 10
    if new_position == 0:
        return 10
    return new_position


@timed_run
def solve(positions):
    scores = tuple(0 for _ in positions)
    wins = count_wins(tuple(positions), scores)
    return max(wins)


if __name__ == '__main__':
    print(solve(read_input()))
