"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0]*(rowIndex + 1)
        res[0] = 1
        res[rowIndex] = 1
        for i in range(1,rowIndex):
            denominator =  numerator = 1
            for item in range(1, i+1):
                denominator = denominator*item 
            for item in range(rowIndex-i+1, rowIndex+1):
                numerator = numerator*item 
            res[i] = numerator//denominator
        return res
        