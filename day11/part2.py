import sys
from lib import timed_run
from itertools import product, count


@timed_run
def read_input():
    octos = list()
    for line in sys.stdin:
        octos.append([int(x) for x in line.strip()])
    return octos


def get_adjacent(row, col, num_rows, num_cols):
    left_bound, right_bound = max((0, row - 1)), min(row + 1, num_rows - 1)
    up_bound, down_bound = max((0, col - 1)), min(col + 1, num_cols - 1)
    return {(r, c) for r in range(left_bound, right_bound + 1) for c in range(up_bound, down_bound + 1)
            if (r, c) != (row, col)}


def increment_octopus(r, c, octos, analysis_queue, already_flashed):
    if (r, c) in already_flashed:
        return 0

    octos[r][c] += 1
    if octos[r][c] > 9:  # flash!
        octos[r][c] = 0
        already_flashed.add((r, c))
        analysis_queue.extend(get_adjacent(r, c, len(octos), len(octos[0])))
        return 1
    return 0


@timed_run
def solve(octos):
    total_octos = len(octos) * len(octos[0])
    for step in count(start=1):
        analysis_queue = list()
        already_flashed = set()

        # everyone gets 1 energy
        for r, c in product(range(len(octos)), range(len(octos[0]))):
            increment_octopus(r, c, octos, analysis_queue, already_flashed)

        # handle flashes
        while analysis_queue:
            r, c = analysis_queue.pop()
            increment_octopus(r, c, octos, analysis_queue, already_flashed)

        if len(already_flashed) == total_octos:  # everyone flashed!
            return step


if __name__ == '__main__':
    print(solve(read_input()))
