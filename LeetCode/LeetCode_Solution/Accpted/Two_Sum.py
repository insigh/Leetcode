class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for i,num in enumerate(nums):
            dict[num]=i
        for i in range (len(nums)):
            opposite=target-nums[i]
            if opposite in dict and dict[opposite]!=i:
                return [i,dict[opposite]]
        return []
