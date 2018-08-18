"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        dict_ = {}
        L = len(heights)
        for i in range(L):
            temp = []
            for j in range(i,L):
                temp.append(min(heights[i:j+1]))
            dict_[i] = temp
        res = 0
        for i,list_ in dict_.items():
            for j,num in enumerate(list_,1):
                res = max(j*num, res)
        return res
            
            