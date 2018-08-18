"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L = len(nums)
        self.res = []
        for k in range(L+1):
            self.getAllcombines(nums,k,0,-1,[])
        return self.res
        
    def getAllcombines(self,nums,k,i,m,ans):
        if i==k :
            if ans not in self.res:
                self.res.append(ans)
        else:
            for j in range(m+1,len(nums)-k+i+1):
                self.getAllcombines(nums,k,i+1,j,ans+[nums[j]])
        
            
            