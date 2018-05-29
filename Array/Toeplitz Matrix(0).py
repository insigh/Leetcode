"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        valid = {}

        flag = True
        for i in range(0, m):
            for j in range(0, n):
                if str(i - j) not in valid.keys():
                    valid[str(i - j)] = matrix[i][j]
                else:
                    if valid[str(i - j)] != matrix[i][j]:
                        return False

        return flag