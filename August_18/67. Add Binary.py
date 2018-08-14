""" 
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
""" 
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_l,b_l = len(a),len(b)
        min_len = min(a_l,b_l)
        max_len = max(a_l,b_l)
        if a_l == min_len:
            min_len = a_l
        else:
            min_len = b_l
        res = ""   
        up = 0
        for i in range(min_len):
            res = str((int(a[-i-1])+int(b[-i-1])+up)%2)+res
            up = ((int(a[-i-1])+int(b[-i-1])+up)//2)
        if min_len == a_l:
            for i in range(min_len,max_len):
                res = str((int(b[-i-1])+up)%2)+res
                up = ((int(b[-i-1])+up)//2)
        else:
            for i in range(min_len,max_len):
                res = str((int(a[-i-1])+up)%2)+res
                up = ((int(a[-i-1])+up)//2)
        if up:
            res = str(up)+res
        
        return res
                
            
           