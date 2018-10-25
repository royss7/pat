#!/usr/local/bin/python3

'''
 ********************************************
 * Description : https://pintia.cn/problem-sets/994805342720868352/problems/994805519074574336
 * Date        : 2018-10-23
 * Author      : liuyy
 * E-mail      : 
 ********************************************
'''

s = 0
for i in input():
    s += int(i)

english = ["zero", "one", "two", "three",
        "four", "five", "six", "seven",
        "eight", "nine"]

ss = [english[int(i)] for i in str(s)]
print(" ".join(ss))


