# encoding:utf-8

import sys

def delete(n_p,A):
    list_people = []
    n_c = len(A)
    for i in range(n_p):
        list_people.append(i)
    count = 1 #  寻找k ，循环轮数,淘汰人数
    i = 0 # 计数开始的位置

    k = 0
    while(count < n_p):
        if list_people[i] != -1:
            k+=1
        if k==A[(count-1)%n_c]:
            list_people[i]=-1
            print(i)
            k=0
            count+=1
        i+=1
        if i==n_p:
            i=0
    for i in range(n_p):
        if list_people[i]!=-1:
            return i

if __name__ == '__main__':
    N =int(sys.stdin.readline().strip())
    tests = []
    for i in range(N):
        line = sys.stdin.readline().strip().split()
        line = [ int(value) for value in line]
        tests.append(line)
    for line in tests:
        n_p = line[0]
        A = line[2:]
        print(delete(n_p,A))
