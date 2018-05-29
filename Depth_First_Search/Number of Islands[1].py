"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        sum = 0
        m, n = len(grid), len(grid[0])

        def dfs(grids, q, r):
            if 0 <= q < m and 0 <= r < n and grids[q][r] == '1':
                grid[q][r] = '0'
                dfs(grids, q + 1, r)
                dfs(grids, q, r + 1)
                dfs(grids, q - 1, r)
                dfs(grids, q, r - 1)
                return 1
            else:
                return 0

        for i in range(m):
            for j in range(n):
                sum += dfs(grid, i, j)

        return sum
