
"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
    
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones=0
        cur_ones=0
        for i in range(0,len(nums)):
            cur_ones= cur_ones+1 if nums[i]==1 else 0
            max_ones=max(max_ones,cur_ones)
        return max_ones