#!/usr/local/bin/python3

'''
 ********************************************
 * Description : https://pintia.cn/problem-sets/994805342720868352/problems/994805502658068480
 * Date        : 2018-10-25
 * Author      : liuyy
 * E-mail      : 
 ********************************************
'''

(n, m) = [int(i) for i in input().split()]
students = []

for i in range(n):
    temp = input().split()
    name = temp[0]
    del temp[0]
    temp = [int(i) for i in temp]
    temp.append(sum(temp) / len(temp))
    students.append([name, temp])

by_c = sorted(students, key = lambda x: x[1][0], reverse = True)
by_m = sorted(students, key = lambda x: x[1][1], reverse = True)
by_e = sorted(students, key = lambda x: x[1][2], reverse = True)
by_a = sorted(students, key = lambda x: x[1][3], reverse = True)
    

