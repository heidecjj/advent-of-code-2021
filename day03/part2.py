import sys
import functools

def rating(numbers, pred):
    candidates = numbers
    for pos in range(len(numbers[0])):
        zeros, ones = list(), list()
        for number in candidates:
            if number[pos] == '0':
                zeros.append(number)
            else:
                ones.append(number)
        candidates = ones if pred(zeros, ones) else zeros
        if len(candidates) == 1:
            break

    return int(candidates[0], 2)





all_numbers = tuple(line.strip() for line in sys.stdin)

oxygen = rating(all_numbers, lambda z, o: len(o) >= len(z))
co2 = rating(all_numbers, lambda z, o: len(o) < len(z))


print(oxygen * co2)
