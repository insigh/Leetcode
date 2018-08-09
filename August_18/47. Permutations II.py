""" 
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        
        L,res = len(nums),[]
        temp = []
        temp[:] = nums[:]
        res.append(temp)
        
        i = L-1
        while i != 0 and nums[i] <= nums[i-1]:
            i -= 1
        while i != 0:
            
            # find the min the bigger than nums[i-1] in the left 
            for j in range(L-1,i-1,-1):
                if nums[j]>nums[i-1]:
                    swap = j
                    break
                    
            # change and reversed the after j
            nums[i-1],nums[swap] = nums[swap],nums[i-1]
            nums[i:]=sorted(nums[i:])
            temp = []
            temp[:] = nums[:]
            res.append(temp)
            
            # find next i for iters 
            i = L-1
            while i !=0 and nums[i] <= nums[i-1]:
                i -= 1
            
    
        return res
            
            
            
            
        
        
            
        
        
        