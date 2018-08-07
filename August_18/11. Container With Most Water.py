"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
 which together with x-axis forms a container, such that the container contains the most water.

 Note: You may not slant the container and n is at least 2.
""" 

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # initial index of left bar and right bar
        L = len(height)
        i = 0 
        j = L-1
        
        max_res = 0
        while i<j:
            if height[i] <= height[j]:
                short_bar = height[i]
                max_res = max(short_bar*(j-i),max_res)
                i += 1
            elif height[i] > height[j]:
                short_bar = height[j]
                max_res = max(short_bar*(j-i),max_res)
                j -= 1
        return max_res

print(Solution().maxArea([4,1,1,1,1,1,8,4]))