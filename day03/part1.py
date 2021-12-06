import sys
import functools

def list_add(one, two):
    return tuple(x + y for x, y in zip(one, two))

def bool_array_to_int(bools):
    return int(''.join('1' if x else '0' for x in bools), 2)


count = 0
sums = None
for line in sys.stdin:
    count += 1
    entry = tuple(int(x) for x in line.strip())
    if sums:
        sums = list_add(sums, entry)
    else:
        sums = entry

gamma = bool_array_to_int(x > count // 2 for x in sums)
epsilon = bool_array_to_int(x < count // 2 for x in sums)

print(gamma * epsilon)
