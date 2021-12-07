import sys


def get_intput():
    return sorted(int(x) for x in sys.stdin.readline().split(','))


def calculate_fuel(position, crabs):
    return int(sum((abs(position - crab) * (abs(position - crab) + 1)) / 2 for crab in crabs))


def minimal_fuel(crabs):
    min_fuel = calculate_fuel(0, crabs)
    for pos in range(crabs[-1] + 1):
        fuel = calculate_fuel(pos, crabs)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


if __name__ == '__main__':
    print(minimal_fuel(get_intput()))
