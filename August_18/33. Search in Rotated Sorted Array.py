"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0,len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -=1
            else:
                if nums[left] <= nums[mid]:
                    if target <= nums[mid] and target >= nums[left]:
                        right -= 1
                    else:
                        left += 1
                else:
                    if target <= nums[right] and target >= nums[mid]:
                        left += 1
                    else:
                        right -= 1
        return -1
        