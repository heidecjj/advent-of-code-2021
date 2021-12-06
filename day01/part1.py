#!/usr/bin/python3
import sys


def main():
    num_increases = 0
    previous = int(sys.stdin.readline())
    for line in sys.stdin:
        current = int(line)
        if current > previous:
            num_increases += 1
        previous = current

    print(num_increases)


if __name__ == '__main__':
    main()
