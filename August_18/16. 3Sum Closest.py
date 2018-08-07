"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        L,res = len(nums),[]
        min_distance = 2147483647
        res = -2147483648
        for i in range(L-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            two_sum = target-nums[i]
            s,e = i+1,L-1
            while s<e:
                if abs((nums[s]+nums[e])- two_sum )<min_distance:
                    min_distance=abs((nums[s]+nums[e])-two_sum)
                    res = (nums[i]+nums[s]+nums[e])
                if (nums[s]+nums[e]) > two_sum :
                    e -= 1
                else:
                    s += 1
        return res
                