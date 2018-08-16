"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = []
        self.getAll_permutes(nums,[])
        return self.res
    
    def getAll_permutes(self,nums,ans):
        if len(ans)==len(nums):
            self.res.append(ans)
        else:
            for item in nums:
                if item not in ans:
                    self.getAll_permutes(nums,ans+[item])