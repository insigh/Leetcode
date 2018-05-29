"""Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
"""


class Solution(object):
    def sort_nums(self, nums, L, R):
        if L >= R:
            return
        temp = nums[L]
        i = L
        j = R
        while (i != j):
            while (nums[j] >= temp and i < j):
                j -= 1
            while (nums[i] <= temp and i < j):
                i += 1
            if (i < j):
                temp1 = nums[i]
                nums[i] = nums[j]
                nums[j] = temp1

        nums[L] = nums[i]
        nums[i] = temp

        self.sort_nums(nums, L, i - 1)
        self.sort_nums(nums, i + 1, R)

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.sort_nums(nums, 0, len(nums) - 1)
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum
