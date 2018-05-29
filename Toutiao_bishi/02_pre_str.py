# -*- coding: utf-8 -*-
"""
input :
7 3
a
bc
d
eba
ebc
f
你好

ebcc
你好么
ebd

6 3 
a
bc
d
eba
ebc
f

yuklx
bcc
ff

7 3
a
bc
d
eba
ebc
f
你好

ebcc
你好么
ebd

6 3 
a
bc
d
eba
ebc
f

yuklx
bcc
ff


 output: 
1
1
-1
-1 
1
1

"""
import sys

def find(seek_str,pre):
    for item in pre.keys():
        if seek_str.startswith(item):
            return 1
    return -1

if __name__ == '__main__':
    while True:
        line1 = sys.stdin.readline().strip().split()
        line1 = [int(item) for item in line1]
        try:
            pre_num = line1[0]
            seek_num = line1[1]
            pre = {}
            seek = []
            for i in range(pre_num):
                line = str(sys.stdin.readline().strip())
                if not pre.has_key(line):
                    pre[line] = 0

            null_line = sys.stdin.readline()
            for i in range(seek_num):
                line = str(sys.stdin.readline().strip())
                seek.append(line)

            for i in range(seek_num):
                print(find(seek[i], pre))
            null_line = sys.stdin.readline()
            print(' ')
        except:
            break

