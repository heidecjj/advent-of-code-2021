import sys
from lib import timed_run
from dataclasses import dataclass
from collections import defaultdict


def rotate_z(direction=1):
    def rotate(point):
        x, y, z = point
        return -direction * y, direction * x, z
    return rotate


def rotate_y(direction=1):
    def rotate(point):
        x, y, z = point
        return -direction * z, y, direction * x
    return rotate


rotations = (
    # top
    rotate_z(1),
    rotate_z(1),
    rotate_z(1),
    # back
    rotate_y(1),
    rotate_z(1),
    rotate_z(1),
    rotate_z(1),
    # left
    rotate_y(1),
    rotate_z(1),
    rotate_z(1),
    rotate_z(1),
    # bottom
    rotate_y(-1),
    rotate_z(1),
    rotate_z(1),
    rotate_z(1),
    # front
    rotate_y(-1),
    rotate_z(1),
    rotate_z(1),
    rotate_z(1),
    # right
    rotate_y(1),
    rotate_z(-1),
    rotate_z(-1),
    rotate_z(-1),
    # top
    rotate_y(-1),
)


@dataclass
class Scanner:
    id: int
    center: list = None
    rotation: int = 0
    beacons: set = None

    @property
    def locked_in(self):
        return self.center is not None

    def rotate(self):
        self.beacons = {rotations[self.rotation](point) for point in self.beacons}
        self.rotation = self.rotation + 1 if self.rotation < 23 else 0


@timed_run
def read_input():
    scanners = list()
    id = 0
    while True:
        scanner = set()
        header = sys.stdin.readline()
        if not header.startswith('---'):
            break
        for line in sys.stdin:
            stripped = line.strip()
            if stripped:
                scanner.add(tuple(int(x) for x in stripped.split(',')))
            else:
                break
        scanners.append(Scanner(id=id, beacons=scanner))
        id += 1
    return scanners


def tuple_sub(one, two):
    return tuple(o - t for o, t in zip(one, two))


def tuple_add(one, two):
    return tuple(o + t for o, t in zip(one, two))


def match(located, workon):
    if not located:
        return False
    for _ in range(24):  # each rotation
        for known_scanner in located:
            for known_pt in known_scanner.beacons:
                for pivot in workon.beacons:  # line up one unknown with known_pt
                    matches = 0  # need to find 12
                    translate = tuple_sub(known_pt, pivot)
                    for other in workon.beacons:
                        if tuple_add(other, translate) in known_scanner.beacons:
                            matches += 1
                        if matches == 12:
                            workon.center = tuple_add(known_scanner.center, translate)
                            return True
        workon.rotate()
    return False


@timed_run
def solve(scanners):
    to_locate = list(scanners)
    located = list()

    origin = to_locate.pop(0)
    origin.center = (0, 0, 0)
    located.append(origin)

    skip = defaultdict(set)  # keep track of failed comparisons so we don't make them again

    while to_locate:
        workon = to_locate.pop(0)
        compare_against = tuple(s for s in located if s.id not in skip[workon.id])
        if match(compare_against, workon):
            located.append(workon)
            print(workon.center)
            return
        else:
            to_locate.append(workon)
            skip[workon.id].update(s.id for s in compare_against)

    truth = set()
    for scanner in located:
        truth.update(tuple(tuple_add(beacon, scanner.center) for beacon in scanner.beacons))
    return len(truth)


if __name__ == '__main__':
    print(solve(read_input()))
