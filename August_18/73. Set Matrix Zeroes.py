"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        M,N = len(matrix),len(matrix[0])
        column = [0 for _ in range(N)]
        row = [0 for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row[i] = 1
                    column[j] = 1
                    
        for i in range(M):
            if row[i]==1:
                for j in range(N):
                    matrix[i][j] = 0
        print(matrix)
        for j in range(N):
            if column[j] == 1:
                for i in range(M):
                    matrix[i][j] = 0
        
                
                