import sys
from lib import timed_run
from collections import defaultdict
from functools import lru_cache


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
    @lru_cache(None)
    def count_paths_to_start(node, seen_small, small_visited_twice):
        if node == 'start':
            return 1

        if node.islower():
            if node in seen_small:
                if small_visited_twice or node == 'end':
                    return 0
                small_visited_twice = True
            seen_small += (node,)

        total = 0
        for neighbor in node_to_neighbors[node]:
            total += count_paths_to_start(neighbor, seen_small, small_visited_twice)
        return total

    return count_paths_to_start('end', tuple(), False)


if __name__ == '__main__':
    print(solve(read_input()))
