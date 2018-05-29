"""In MATLAB, there is a very useful function called 'reshape', 
which can reshape a matrix into a new one with different size but 
keep its original data.


You're given a matrix represented by a two-dimensional array,
 and two positive integers r and c representing 
 the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums

        new_array = [item for row in nums for item in row]

        res = []
        for i in range(0, m * n, c):
            row = []
            row.extend(new_array[i:i + c])
            res.append(row)
        return res