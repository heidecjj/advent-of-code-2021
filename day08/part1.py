import sys
from lib import timed_run


@timed_run
def read_input():
    notes = list()
    for line in sys.stdin:
        left, right = line.split('|')
        notes.append((left.split(), right.split()))
    return notes


@timed_run
def count_unique(notes):
    return sum(sum(len(digit) in (2, 3, 4, 7) for digit in right) for _, right in notes)


if __name__ == '__main__':
    print(count_unique(read_input()))
