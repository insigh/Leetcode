"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, num):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if num >= 1:
            res.append([1])
        if num >= 2:
            res.append([1,1])
        if num > 2:
            
            left = 0
            right = 0
            for i in range(2,num):
                temp = []
                prev = res[-1]
                temp.append(prev[0])
                for j in range(i-1):
                    temp.append(prev[j]+prev[j+1])
                temp.append(prev[-1])
                res.append(temp)
        return res
                
    
        