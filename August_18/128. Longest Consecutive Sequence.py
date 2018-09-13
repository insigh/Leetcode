"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0

        for n in nums:
            if n - 1 in nums:
                continue

            m = n + 1
            while m in nums:
                m += 1
            res = max(res, m - n)
        return res

    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        dict_ = {}
        res = 0
        for num in nums:
            if num not in dict_.keys():

                left = dict_.get(num - 1) if dict_.get(num - 1) else 0
                right = dict_.get(num + 1) if dict_.get(num + 1) else 0
                sum_ = left + right + 1
                dict_[num] = sum_

                res = max(res, sum_)

                dict_[num - left] = sum_
                dict_[num + right] = sum_
            else:

                continue

        return res