"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

"""
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        sequence = [False for i in range(n)]
        self.res = [0]
        self.getAllcode(0,n,sequence)
        return self.res
        
        
    def getAllcode(self,cur,n,sequence):
        if len(self.res) == 2**n:
            return 
        for i in range(n):
            if not sequence[i] and cur+2**i not in self.res and (cur+2**i)<2**n:
                sequence[i] = True
                self.res.append(cur+2**i)
                self.getAllcode(cur+2**i,n,sequence)
                
            elif sequence[i] and cur-2**i not in self.res and cur-2**i>0:
                sequence[i] = False
                self.res.append(cur-2**i)
                self.getAllcode(cur-2**i,n,sequence)
                sequence[i] = True
                
        
        