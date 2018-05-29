#coding=utf-8
import sys


def longestValidParentheses( s):
    # using stack
    sta = []
    max_l = 0
    l = 0
    for i, str_i in enumerate(s):
        l += 1

        if str_i is '(':
            sta.append(i)
        else:
            if sta:
                sta.pop()
            else:
                l = 0
        if sta:
            max_l = max(max_l, i - sta[-1])
        else:
            max_l = max(max_l, l)

    return max_l

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    lines = [line.strip().split() for line in lines]
    print(lines)




