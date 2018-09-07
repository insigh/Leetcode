"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rank = [ index for index,item in sorted(enumerate(nums),key=lambda x:x[1])]
        nums = sorted(nums)
        s,e = 0,len(nums)-1
        res = []
        while s<e:
            if nums[s]+nums[e]==target:
                res.append([rank[s],rank[e]]) 
                s += 1 
                while s<e and nums[s]==nums[s-1]:
                    s += 1
            elif nums[s]+nums[e]<target:
                s += 1
            else :
                e -= 1
        assert len(res)==1
        return res[0]
            
        
                    
        