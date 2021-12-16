import sys
from lib import timed_run


@timed_run
def read_input():
    lines = list()
    for line in sys.stdin:
        lines.append(tuple(int(x) for x in line.strip()))
    return lines


def dijkstra(graph):
    distance_from_start = dict()
    distance_from_start[(0, 0)] = 0
    optimized = set()

    max_r, max_c = len(graph), len(graph[0])

    end = (max_r - 1, max_c - 1)
    while end not in optimized:
        min_coord = find_min_coord(distance_from_start, optimized)
        optimized.add(min_coord)
        update_neighbors(min_coord, distance_from_start, graph, max_r, max_c)

    return distance_from_start[end]


def find_min_coord(distances, optimized):
    minimum_coord = None
    for key, value in distances.items():
        if key in optimized:
            continue
        if not minimum_coord:
            minimum_coord, minimum_value = key, value
        elif value < minimum_value:
            minimum_coord, minimum_value = key, value
    return minimum_coord


def update_neighbors(coord, distance_from_start, graph, max_r, max_c):
    r, c = coord
    coord_dist = distance_from_start[coord]
    for r_, c_ in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)):
        if -1 < r_ < max_r and -1 < c_ < max_c:
            neighbor_dist = distance_from_start.get((r_, c_))
            neighbor_through_coord = coord_dist + graph[r_][c_]
            if neighbor_dist is None or neighbor_dist > neighbor_through_coord:
                distance_from_start[(r_, c_)] = neighbor_through_coord


@timed_run
def solve(graph):
    return dijkstra(graph)


if __name__ == '__main__':
    print(solve(read_input()))
