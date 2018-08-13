"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # if not obstacleGrid or obstacleGrid[0][0] or obstacleGrid[1][1]:
        #     return 0
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif j == n-1 and i<m-1 :
                    dp[i][j] = dp[i+1][j]
                elif i == m-1 and j<n-1 :
                    dp[i][j] = dp[i][j+1]
                elif i==m-1 and j==n-1:
                    dp[i][j] = 1-obstacleGrid[m-1][n-1]
                else:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j]
                        
        
        return dp[0][0]
        
        
    
        
            
            
            