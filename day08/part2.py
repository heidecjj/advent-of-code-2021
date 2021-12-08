import sys
from lib import timed_run


@timed_run
def read_input():
    notes = list()
    for line in sys.stdin:
        left, right = line.split('|')
        notes.append((left.split(), right.split()))
    return notes


def decode_digit(decoder, digit):
    return decoder[''.join(sorted(digit))]


def contains_glyph(digit, glyph):
    return all(c in digit for c in glyph)


def discover_decoder(digits):
    decoder = dict()
    digits = list(''.join(sorted(digit)) for digit in sorted(digits, key=len))

    one = digits[0]
    four = digits[2]
    elbow = ''.join(sorted(set(four) - set(one)))

    decoder[one] = 1
    decoder[digits[1]] = 7
    decoder[four] = 4
    decoder[digits[-1]] = 8

    for digit in digits:
        if len(digit) == 6:
            if contains_glyph(digit, one):  # 9 or 0
                if contains_glyph(digit, elbow):
                    decoder[digit] = 9
                else:
                    decoder[digit] = 0
            else:
                decoder[digit] = 6
        elif len(digit) == 5:
            if contains_glyph(digit, one):
                decoder[digit] = 3
            else:
                if contains_glyph(digit, elbow):
                    decoder[digit] = 5
                else:
                    decoder[digit] = 2

    return decoder


def decode(decoder, digits):
    return int(''.join(str(decode_digit(decoder, d)) for d in digits))


@timed_run
def find_answer(notes):
    total = 0
    for left, right in notes:
        decoder = discover_decoder(left)
        total += decode(decoder, right)
    return total


if __name__ == '__main__':
    print(find_answer(read_input()))
