"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

"""
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix :
            return 0
        h_list = [[1 if item=='1' else 0 for item in matrix[0]] ]
        # print(h_list)
        for i in range(1,len(matrix)):
            heights = []
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    heights.append(0)
                else:
                    heights.append(h_list[-1][j]+1)
            h_list.append(heights)
        res = 0
        for heights in h_list:
            res = max(res,self.largestRetangleArea(heights))
        return res
                    
            
            
            
    def largestRetangleArea(self,heights):
        stack = []
        heights.append(0)
        res = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                temp = stack.pop()
                dist = i if not stack else i - stack[-1] -1
                res = max(res,dist*heights[temp])
                i -= 1
            i += 1 
        return res
        