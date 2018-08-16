class Solution(object):
	"""docstring for ClassName"""
	
	def quicksort(self,nums):
		L = len(nums)
		self.partition(nums,0,L-1)
		return nums
	def partition(self,nums,low,high):
		if low < high:
			pivot = nums[high]
			i,j = low,low
			for j in range(low,high):
				if nums[j] < pivot:
					nums[i],nums[j] = nums[j],nums[i]
					i += 1
			nums[i],nums[high] = nums[high],nums[i]
			self.partition(nums,i+1,high)
			self.partition(nums,0,i-1)

print(Solution().quicksort(nums=[98,7,25265,26,5]))