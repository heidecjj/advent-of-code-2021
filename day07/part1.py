import sys


def get_intput():
    return sorted(int(x) for x in sys.stdin.readline().split(','))


def calculate_fuel(position, crabs):
    return sum(abs(position - crab) for crab in crabs)


def minimal_fuel(crabs):
    return calculate_fuel(crabs[len(crabs)//2], crabs)


if __name__ == '__main__':
    print(minimal_fuel(get_intput()))
