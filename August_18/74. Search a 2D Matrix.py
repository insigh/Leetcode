"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M = len(matrix)
        if M== 0:
            return False
        N = len(matrix[0])
        if N == 0:
            return False

        
        last_column = [ matrix[i][N-1] for i in range(M)]
        # print(first_column)
        i = 0
        while i < M-1 and target>last_column[i]:
            i += 1
        # print(i)
        for j in range(N):
            if matrix[i][j] == target:
                return True
        return False
            
            