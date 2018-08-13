"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution(object):
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.helper(m,n)
    
    
    def helper(self,m,n):
        numerator = 1
        for i in range(m+n-2,m-1,-1):
            numerator *= i
        denominator = 1
        for j in range(n-1,0,-1):
            denominator *= j
        return numerator/denominator
        
        
        