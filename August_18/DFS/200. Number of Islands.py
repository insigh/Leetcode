"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j, grid):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i + 1, j, grid)
                dfs(i - 1, j, grid)
                dfs(i, j + 1, grid)
                dfs(i, j - 1, grid)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j, grid)
        return count
