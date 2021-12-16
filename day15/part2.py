import sys
from lib import timed_run
from copy import copy
import heapq


@timed_run
def read_input():
    lines = list()
    for line in sys.stdin:
        lines.append([int(x) for x in line.strip()])
    return lines


def dijkstra(graph):
    dist = dict()
    dist[(0, 0)] = 0
    frontier = []
    entry_finder = dict()

    entry = [0, (0, 0)]
    entry_finder[(0, 0)] = entry
    heapq.heappush(frontier, entry)
    DELETED = (-1, -1)

    max_r, max_c = len(graph), len(graph[0])

    end = (max_r - 1, max_c - 1)
    while True:
        cost, node = heapq.heappop(frontier)
        if node == DELETED:
            continue

        if node == end:
            return cost

        for neighbor in get_neighbors(node, max_r, max_c):
            alt = dist[node] + graph[neighbor[0]][neighbor[1]]
            dist_neighbor = dist.get(neighbor)

            if dist_neighbor is None or alt < dist_neighbor:
                dist[neighbor] = alt

                if dist_neighbor in entry_finder:
                    entry = entry_finder.pop(neighbor)
                    entry[-1] = DELETED

                new_entry = [alt, neighbor]
                entry_finder[neighbor] = new_entry
                heapq.heappush(frontier, new_entry)


def get_neighbors(coord, max_r, max_c):
    r, c = coord
    return tuple((r_, c_) for r_, c_ in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)) if -1 < r_ < max_r and -1 < c_ < max_c)


def expand_graph(graph):
    new_graph = copy(graph)
    for inc in range(1, 5):  # copy down
        for row in graph:
            new_graph.append([x + inc if x + inc < 10 else x + inc - 9 for x in row])

    for row in new_graph:  # copy right
        original_row = copy(row)
        for inc in range(1, 5):
            row.extend([x + inc if x + inc < 10 else x + inc - 9 for x in original_row])

    return new_graph


@timed_run
def solve(graph):
    return dijkstra(graph)


if __name__ == '__main__':
    print(solve(expand_graph(read_input())))
