""""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L =len(nums)
        self.res = []
        for i in range(L+1):
            self.getAllcombines(nums,i,0,-1,[])
        return self.res
    def getAllcombines(self,nums,k,i,m,ans):
        if i==k:
            self.res.append(ans)
        else:
            for j in range(m+1,len(nums)-k+i+1):
                self.getAllcombines(nums,k,i+1,j,ans+[nums[j]])
                
        
        
        