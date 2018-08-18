"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        
        """
        
        stack = []
        heights.append(0)
        res = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
                
            else:
                temp = stack.pop()
                res = max(res,heights[temp]*(i if not stack else i - stack[-1] -1))
                i -= 1
                
            i += 1
        return res