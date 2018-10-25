#!/usr/local/bin/python3

'''
 ********************************************
 * Description : 
 * Date        : 2018-10-24
 * Author      : liuyy
 * E-mail      : 
 ********************************************
'''

(n1, n2, tag, radix) = input().split()

tag = int(tag)
radix = int(radix)

m = {i[1] : i[0] for i in enumerate('0123456789abcdefghijklmnopqrstuvwxyz')}
def parse(s, radix):
    val = 0
    r = 1
    for i in s[::-1]:
        val += m[i] * r
        r *= radix
    
    return val

if tag == 2:
    (n1, n2) = (n2, n1)

if radix < max(iter([m[i] for i in n1])) + 1:
    print("Impossible")
else:

    n1 = parse(n1, radix)

    min_radix = max(iter([m[i] for i in n2])) + 1
    find = False
    while not find:
        mid = (min_radix + n1) // 2

    for i in range(min_radix, 37):
        t = parse(n2, i)
        if n1 == t:
            print(i)
            find = True
            break
        elif t > n1:
            break

    if not find:
        print("Impossible")
