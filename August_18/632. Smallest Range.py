"""
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
"""
class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        L,R = None,None
        
        while True:
            mn=mx = nums[0][-1]
            ids = [0]
            for i in range(1,len(nums)):
                if nums[i][-1] > mx:
                    mx,ids = nums[i][-1],[i]
                elif nums[i][-1] < mn:
                    mn = nums[i][-1]
                elif nums[i][-1] == mx:
                    ids.append(i)
            # print(mn,mx)
            if not L or mx-mn <= R-L:
                L,R = mn,mx
            for j in ids:
                nums[j].pop()
                if not nums[j]:
                    return [L,R]
                
        
        