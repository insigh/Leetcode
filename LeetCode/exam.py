#coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    line = sys.stdin.readline().strip()
    # 把一行的数字分隔后转化成int列表
    values = map(int, line.split())
    x,y=values[0],values[1]
    map= [[[-1 for col in range(100002)] for row in range(9)]for c in range(9)]
    def search(x,y,k):
        if x==0 and y==0 and k==0:
            map[0][0][0]=1
            return 1
        if x<0 or y<0 or k<0 or x>=8 or y>=8 or k>=100000:
            return 0
        if map[x][y][k] != -1:
            return map[x][y][k]
        map[x][y][k] = (
        search(x + 1, y + 2, k - 1) + search(x + 2, y + 1, k - 1) + search(x + 2, y - 1, k - 1) + search(x + 1, y - 2,
                                                                                                         k - 1) +
        search(x - 1, y - 2, k - 1) + search(x - 2, y - 1, k - 1) + search(x - 2, y + 1, k - 1) + search(x - 1, y + 2,
                                                                                                         k - 1))
        return map[x][y][k]
    print (search(x,y,n)% 1000000007)