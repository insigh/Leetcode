"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if s == 0 or sum(nums)<s:
            return 0
        
        accsum = 0
        i=I=J=0
        for j,num in enumerate(nums,1):
            accsum += num
            print(accsum)
            if accsum >= s:
                while accsum-nums[i]>=s:
                    accsum -= nums[i]
                    i += 1
                if not J or j-i<J-I:
                    I,J = i,j
        print(I,J)
        return J-I

        