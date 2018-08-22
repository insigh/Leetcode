"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        for i in range(1,len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1,len(triangle[i])-1):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j]) 
            triangle[i][len(triangle[i])-1] += triangle[i-1][len(triangle[i])-2]
        return min(triangle[len(triangle)-1])
            
            
            
            
            