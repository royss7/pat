#!/usr/bin/env python3

max_N = 1000 + 1

def parse():
    input_str = input().split()

    res = [0] * max_N
    for i in range(1, len(input_str), 2):
        poly = int(input_str[i])
        k = float(input_str[i+1])

        res[poly] = k

    return res

first = parse()
second = parse()

s = [i[0] + i[1] for i in zip(first, second)]

count_non_zero = max_N - s.count(0)

if count_non_zero == 0:
    print(0)
else:
    print(count_non_zero, end = "")
    for i in range(len(s)-1, -1, -1):
        if s[i] != 0:
            print(" {0} {1:.1f}".format(i, s[i]), end = "") 
    print()
