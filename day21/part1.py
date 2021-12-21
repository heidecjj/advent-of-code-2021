import sys
from lib import timed_run


@timed_run
def read_input():
    lines = list()
    for line in sys.stdin:
        lines.append(int(line.split(': ')[1].strip()))
    return lines


def deterministic_die():
    num = 1
    while True:
        yield num
        num = num + 1 if num < 100 else 1


@timed_run
def solve(positions):
    scores = [0 for _ in positions]
    die = deterministic_die()
    num_rolls = 0
    winner = None

    while winner is None:
        for player in range(len(positions)):
            advance = next(die) + next(die) + next(die)
            num_rolls += 3
            new_position = (positions[player] + advance) % 10
            if new_position == 0:
                new_position = 10
            scores[player] += new_position
            positions[player] = new_position
            if scores[player] >= 1000:
                winner = player
                break

    loser = 0 if winner else 1
    return scores[loser] * num_rolls


if __name__ == '__main__':
    print(solve(read_input()))
