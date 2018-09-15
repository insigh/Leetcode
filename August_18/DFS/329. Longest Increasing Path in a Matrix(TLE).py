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
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

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
        ascend = [[1 for i in range(n)] for j in range(m)]
        self.res = 0
        self.visited = [[False for i in range(n)] for j in range(m)]

        def dfs(i, j, matrix, step):

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            self.visited[i][j] = max(step, self.visited[i][j])
            if step < self.visited[i][j]:
                return

            if not (i < m - 1 and matrix[i + 1][j] > matrix[i][j]) and not (
                    i > 0 and matrix[i - 1][j] > matrix[i][j]) and not (
                    j > 0 and matrix[i][j - 1] > matrix[i][j]) and not (j < n - 1 and matrix[i][j + 1] > matrix[i][j]):
                self.res = max(self.res, step)
                return

            if i < m - 1 and matrix[i + 1][j] > matrix[i][j]:
                if self.visited[i + 1][j] < step + 1:
                    dfs(i + 1, j, matrix, step + 1)
            if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                if self.visited[i - 1][j] < step + 1:
                    dfs(i - 1, j, matrix, step + 1)
            if j > 0 and matrix[i][j - 1] > matrix[i][j]:
                if self.visited[i][j - 1] < step + 1:
                    dfs(i, j - 1, matrix, step + 1)
            if j < n - 1 and matrix[i][j + 1] > matrix[i][j]:
                if self.visited[i][j + 1] < step + 1:
                    dfs(i, j + 1, matrix, step + 1)

        for i in range(m):
            for j in range(n):
                if not self.visited[i][j]:
                    dfs(i, j, matrix, 1)

        return self.res


