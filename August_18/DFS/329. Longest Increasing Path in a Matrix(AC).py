"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
"""


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = 0
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        self.m, self.n = m, n
        self.cache = [[0 for i in range(n)] for j in range(m)]
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j, matrix):
            if self.cache[i][j]:
                return self.cache[i][j]

            max_ = 1
            for item in self.dirs:
                x, y = i + item[0], j + item[1]
                if x < 0 or x >= self.m or y < 0 or y >= self.n or matrix[x][y] <= matrix[i][j]:
                    continue
                len_ = 1 + dfs(x, y, matrix)
                max_ = max(max_, len_)
            self.cache[i][j] = max_
            return max_

        res = 1
        for i in range(m):
            for j in range(n):
                len_ = dfs(i, j, matrix)
                res = max(len_, res)

        return res




