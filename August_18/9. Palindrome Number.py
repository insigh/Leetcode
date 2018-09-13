"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        ret = True 
        if x < 0:
            ret = False
        
        else:
            ranger = 1
            while x / ranger >= 10:
                ranger *= 10
            
            while x:
                left = x / ranger
                right = x % 10
                if left != right:
                    ret =False
                
                x = (x % ranger)/10
                ranger /= 100
                
        return ret
            
        