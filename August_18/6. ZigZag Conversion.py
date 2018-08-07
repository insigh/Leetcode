"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR" 

"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        ans = ["" for _ in range(numRows)]
        direction = 1 # initial direction to next moving 
        row = 0 # initial row number 
        
        while s:
            ans[row] += s[0]
            s = s[1:]
            row += direction 
            if row == 0 or row == numRows-1:
                direction *= -1
            
        return "".join(ans)

print(Solution().convert(s="PAYPALISHIRING", numRows=3))