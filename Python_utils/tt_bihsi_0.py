# encoding:utf-8
"""
对于严格递增的正整数数列A=a1,a2,...an,如果一个正整数T满足：
(1): 对于A中的任意一个数，如果x+T不大于an,则x+T 也是数列中的数
(2): 对于A中的任意一个数，如果x-T不小于a1,则x-T 也是数列中的数
那么T为数列A的周期，如果同时满足：
(3):所有小于T的正整数，都不是T的周期
则T为A的最小正周期
输入n个数列，求出他们的最小正周期
输入：
3
3 1 2 3 
3 2 4 6
3 3 4 6 7 9 10
输出：
1
2
3

"""
import sys


def min_T(A):
    min_ = A[0]
    max_ = A[-1]
    size = len(A)
    gaps1 = [(A[-1]-item) for item in A]
    gaps0 = [(item - A[0]) for item in A]
    gap = max_ - min_
    for i in range(1,gap+1):
        flag = True
        for item in range(0,gap+1,i):
            if item not in gaps1 or item not in gaps0:
                flag = False
                break
        if flag:
            return i

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    As = []
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        line = [int(item) for item in line]
        As.append(line[1:])
    for line in As:
        T = min_T(line)
        print(T)
