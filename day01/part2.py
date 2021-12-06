#!/usr/bin/python3
import sys


def main():
    num_increases = 0
    window = list()
    for _ in range(3):
        window.append(int(sys.stdin.readline()))
    window.append(0)
    windex = 0
    for line in sys.stdin:
        window[windex - 1] = int(line)
        if window[windex - 1] > window[windex]:
            num_increases += 1
        windex = (windex + 1) % 4

    print(num_increases)


if __name__ == '__main__':
    main()
