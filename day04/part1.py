import sys
from collections import namedtuple

Card = namedtuple('Card', 'board dots')


def find_square(board, num):
    for r_idx, row in enumerate(board):
        for c_idx, col in enumerate(row):
            if col == num:
                return r_idx, c_idx
    return -1, -1


def mark_number(card, num):
    r, c = find_square(card.board, num)
    if r != -1:
        card.dots[r][c] = True


def is_bingo(card):
    dots = card.dots
    if any(all(row) for row in dots):
        return True
    return any(all(dots[r][c] for r in range(len(dots))) for c in range(len(dots)))


def get_sum_unmarked(card):
    board, dots = card
    total = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if not dots[r][c]:
                total += board[r][c]
    return total


def read_input():
    numbers = [int(x) for x in sys.stdin.readline().split(',')]

    cards = list()

    while True:
        sys.stdin.readline()
        board_ = [[int(x) for x in sys.stdin.readline().split()] for _ in range(5)]
        if not board_[0]:
            break

        dots_ = [[False] * 5 for _ in range(5)]

        cards.append(Card(board_, dots_))

    return numbers, cards


def play_bingo(numbers, cards):
    for called in numbers:
        for card in cards:
            mark_number(card, called)
            if is_bingo(card):
                return called * get_sum_unmarked(card)
    return 0


print(play_bingo(*read_input()))
