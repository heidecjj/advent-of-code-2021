import sys
from lib import timed_run
from collections import defaultdict


@timed_run
def read_input():
    node_to_neighbors = defaultdict(set)
    for line in sys.stdin:
        left, right = line.strip().split('-')
        node_to_neighbors[left].add(right)
        node_to_neighbors[right].add(left)
    return {k: tuple(v) for k, v in node_to_neighbors.items()}


@timed_run
def solve(node_to_neighbors):
    paths = get_to_end('start', tuple(), node_to_neighbors)
    return len(paths)


def get_to_end(node, path, node_to_neighbors, small_visited_twice=False):
    # returns [path, path, path, ...] where path is a tuple(string)
    next_path = path + (node,)
    if node == 'end':
        return [next_path]

    if node.islower() and node in path:
        if node not in ('start', 'end') and not small_visited_twice:
            small_visited_twice = True
        else:
            return list()

    paths = list()
    for neighbor in node_to_neighbors[node]:
        paths.extend(get_to_end(neighbor, next_path, node_to_neighbors, small_visited_twice))
    return paths


if __name__ == '__main__':
    print(solve(read_input()))
