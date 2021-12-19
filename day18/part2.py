import sys
from lib import timed_run
from copy import deepcopy
from dataclasses import dataclass
from itertools import product


@dataclass
class Node:
    left: object = None
    right: object = None
    value: int = None

    @property
    def is_leaf(self):
        return self.value is not None

    def __str__(self):
        if self.is_leaf:
            return str(self.value)
        return f'[{self.left}, {self.right}]'


@timed_run
def read_input():
    for line in sys.stdin:
        yield eval(line.strip())


def snail_add(left, right):
    new = Node(left=left, right=right)
    answer = snail_reduce(new)
    return answer


def snail_reduce(snail):
    found = True
    while found:
        found = snail_explode(snail)
        if found:
            continue
        found, snail = snail_split(snail)

    return snail


def snail_explode(snail):
    nodes = list()

    found = snail_explode_helper(snail, 0, nodes, False)

    if found:
        index = nodes.index(SENTINEL)

        left_of_snail, exploded, right_of_snail = index - 1, index + 1, index + 2
        exploded = nodes[exploded]
        if left_of_snail > -1:
            nodes[left_of_snail].value += exploded.left.value
        if right_of_snail < len(nodes):
            nodes[right_of_snail].value += exploded.right.value
        exploded.left = exploded.right = None

    return found


SENTINEL = 'SENTINEL'


def snail_explode_helper(snail, depth, nodes, found):
    if snail.is_leaf:
        nodes.append(snail)
        return found

    if not found and depth == 4:  # explode
        snail.value = 0
        nodes.append(SENTINEL)
        nodes.append(snail)
        found = True
        return found

    left = snail_explode_helper(snail.left, depth + 1, nodes, found)
    found = found or left
    right = snail_explode_helper(snail.right, depth + 1, nodes, found)
    return found or right


def snail_split(snail):
    if snail.is_leaf:
        if snail.value > 9:
            half = snail.value // 2
            return True, Node(left=Node(value=half), right=Node(value=snail.value - half))
        return False, snail

    found, snail.left = snail_split(snail.left)
    if found:
        return found, snail

    found, snail.right = snail_split(snail.right)
    return found, snail


def snail_magnitude(snail):
    if snail.is_leaf:
        return snail.value
    left, right = snail.left, snail.right
    return 3 * snail_magnitude(left) + 2 * snail_magnitude(right)


def treeify(snail):
    if isinstance(snail, int):
        return Node(value=snail)
    return Node(left=treeify(snail[0]), right=treeify(snail[1]))


@timed_run
def solve(lines):
    snails = list()
    for snail in lines:
        snails.append(treeify(snail))

    mags = list()
    for snail1, snail2 in product(snails, snails):
        if snail1 == snail2:
            continue
        mags.append(snail_magnitude(snail_add(deepcopy(snail1), deepcopy(snail2))))

    return max(mags)


if __name__ == '__main__':
    print(solve(read_input()))
