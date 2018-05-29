# encoding:utf-8
"""
20
20
34  0   0   0   0   0   0   0   0   0   0   0   0   0   0   10  0   0   0   30
0   23  10  5   5   0   0   0   5   5   5   5   5   0   0   0   30  0   40  0
0   9   0   0   5   0   0   0   4   4   4   4   4   0   0   0   0   30  0   0
0   8   7   7   0   5   0   0   3   3   3   3   0   0   0   0   7   0   9   0
0   9   0   0   5   0   5   0   0   12  12  0   0   0   0   10  0   0   0   9
0   0   0   0   5   0   0   5   0   12  12  0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   12  12  0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0
40  30  3   6   6   0   0   0   0   0   0   0   0   5   5   0   0   0   10  0
0   0   20  0   0   6   6   0   0   0   0   0   0   0   5   6   5   10  10  0
40  30  3   7   6   0   0   0   0   0   0   0   0   0   0   6   0   0   10  0
0   0   0   0   0   0   0   17  0   0   0   0   17  0   0   6   5   7   7   0
0   0   0   0   0   0   0   0   7   0   0   7   0   0   0   0   0   0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   30  0   7   0   0   0   0   0   5   5   0   0   0   0   0   0   10  0   50
0   40  7   0   0   0   0   0   0   5   5   0   0   0   0   0   0   0   50  0
43  30  25  10  50  0   0   0   6   6   6   6   0   0   0   0   0   50  0   0
我
323
116
"""

import sys

# def strengths( grid):
#     if len(grid) == 0:
#         return 0
#     m, n = len(grid), len(grid[0])
#
#     def dfs(grid, i, j):
#         strength = 0
#         if (0 <= i < m and 0 <= j < n and grid[i][j] != 0 ):
#             strength += grid[i][j]
#             grid[i][j] = 0
#             dfs(grid, i + 1, j)
#             dfs(grid, i, j + 1)
#             dfs(grid, i - 1, j)
#             dfs(grid, i, j - 1)
#             return strength
#         else:
#             return 0
#
#     res = []
#     for i in range(m):
#         for j in range(n):
#             if dfs(grid,i,j) > 0:
#                 res.append( dfs(grid,i,j))
#
#     return max(res),min(res)

def strengths(grid):
    m, n = len(grid), len(grid[0])
    def dfs(grid, i, j):
        if (0 <= i < m and 0 <= j < n and grid[i][j]!=0):
            strength = grid[i][j]
            grid[i][j] = 0
            return strength + dfs(grid, i - 1, j) + dfs(grid, i, j - 1) + dfs(grid, i + 1, j) + dfs(grid, i, j + 1)\
                               +dfs(grid,i-1,j-1) + dfs(grid, i-1, j + 1) + dfs(grid, i + 1, j-1) + dfs(grid, i+1, j + 1)
        else:
            return 0

    areas = [dfs(grid, i, j) for i in range(m) for j in range(n) if grid[i][j]>0 ]

    return (max(areas),min(areas),areas) if areas else (0,0,0)

if __name__ == '__main__':
    row_num = int(sys.stdin.readline().strip())
    col_num = int(sys.stdin.readline().strip())
    grid = []
    for i in range(row_num):
        row_strengths = sys.stdin.readline().strip().split()
        row_strengths = [int(value) for value in row_strengths]
        grid.append(row_strengths)
    max_strength,min_strength,strengths = strengths(grid)
    print(strengths)
    print(max_strength)
    print(min_strength)



