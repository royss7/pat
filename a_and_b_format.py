#!/usr/bin/evn python3

(a, b) = [int(i) for i in input().split()]

s = a + b

if s == 0:
    print(0)
else:
    sign = 1 if s >= 0 else -1
    s *= sign

    sum_to_str = []
    while s > 0:
        sum_to_str.append(s % 1000)
        s //= 1000
    sum_to_str[-1] *= sign

    ss = ["{0:03d}".format(i) for i in sum_to_str[:-1]]
    ss.append("{0}".format(sum_to_str[-1]))
    print(",".join(ss[::-1]))