import sys
from lib import timed_run


@timed_run
def read_input():
    lines = list()
    replacements = sys.stdin.readline().strip()
    sys.stdin.readline()
    for line in sys.stdin:
        lines.append(line.strip())
    return replacements, lines


def extend_image(image, num_iterations):
    dots_to_add = 3 * num_iterations
    new_image = ['.' * (len(image[0]) + 2 * dots_to_add) for _ in range(dots_to_add)]

    new_image += ['.' * dots_to_add + line + '.' * dots_to_add for line in image]

    new_image += ['.' * (len(image[0]) + 2 * dots_to_add) for _ in range(dots_to_add)]

    return new_image


def process_image(image, replacements):
    new_image = list()
    for r_idx, row in enumerate(image):
        if r_idx in (0, len(image) - 1):
            continue
        new_row = ''
        for c_idx in range(len(row)):
            if c_idx in (0, len(image[0]) - 1):
                continue
            left, right = c_idx - 1, c_idx + 2
            lookup_string = image[r_idx - 1][left:right] + row[left:right] + image[r_idx + 1][left:right]
            idx = int(lookup_string.replace('.', '0').replace('#', '1'), base=2)
            new_row += replacements[idx]
        new_image.append(new_row)
    return new_image


@timed_run
def solve(replacements, image):
    new_image = extend_image(image, 2)
    new_image = process_image(new_image, replacements)
    new_image = process_image(new_image, replacements)
    return sum(line.count('#') for line in new_image)


if __name__ == '__main__':
    print(solve(*read_input()))
