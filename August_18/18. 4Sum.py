"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        L,res = len(nums),[]
        for i in range(L-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            three_sum = target-nums[i]
            left_nums = nums[i+1:L]
            triple_list = self.threeSum(left_nums,three_sum)
            print(triple_list)
            for triple in triple_list:
                k,l,m = triple
                res.append([nums[i],k,l,m])
        return res
        
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L,res = len(nums),[]
        for i in range(L-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            two_sum = target-nums[i]
            s,e = i+1,L-1
            while s<e:
                if nums[s]+nums[e]==two_sum:
                    res.append([nums[i],nums[s],nums[e]])
                    s += 1
                    while s<e and nums[s]==nums[s-1]:
                        s += 1
                elif nums[s]+nums[e]<two_sum:
                    s+=1
                else:
                    e-=1
        return res
