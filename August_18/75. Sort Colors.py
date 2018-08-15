"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, low=0, high=len(nums)-1)

    def quicksort(self,nums,low,high):
    	if low < high:
    		p = self.partition(nums,low,high)
    		self.quicksort(nums,low,p-1)
    		self.quicksort(nums,p+1,high)

    def partition(self,nums,low,high):
    	pivot = nums[high]
    	i = low
    	for j in range(low,high):
    		if nums[j] < pivot:
    			nums[i],nums[j] = nums[j],nums[i]
    			i += 1
    	nums[i],nums[high] = nums[high],nums[i]
    	return i

nums = [7348,734,83846,436647,0,3,1,0,3,56]
Solution().sortColors(nums)
print(nums)
