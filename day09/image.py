import sys
from argparse import ArgumentParser
from collections import defaultdict
from functools import reduce


def convert_to_ppm():
    lines = list()
    for line in sys.stdin:
        lines.append(tuple('255 255 255' if x != '9' else '0 0 0' for x in line.strip()))

    print('P3')
    print(f'{len(lines[0])} {len(lines)}')
    print('255')
    for line in lines:
        print(' '.join(line))


def solve():
    sys.stdin.readline()  # type
    sys.stdin.readline()  # comment
    sys.stdin.readline()  # size
    sys.stdin.readline()  # max value

    counts = defaultdict(int)

    for line in sys.stdin:
        nums = tuple(int(x) for x in line.split())
        for r, g, b in zip(nums[::3], nums[1::3], nums[2::3]):
            counts[(r, g, b)] += 1

    del counts[(0, 0, 0)]
    try:
        del counts[(255, 255, 255)]
    except KeyError:
        pass

    print(reduce(lambda x, y: x * y, sorted(counts.values(), reverse=True)[:3]))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('action', choices=['ppm', 'solve'])
    ns = parser.parse_args()
    if ns.action == 'ppm':
        convert_to_ppm()
    else:
        solve()
