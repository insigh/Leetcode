"""
Implement atoi which converts a string to an integer.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_ = str.strip()
        str_ = re.findall("^([\-\+]?\d+)\D*", str_)
        if not str_:
            return 0
        
        if str_:
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            res = int(str_[0])
            if res >= MAX_INT:
                return MAX_INT
            elif res <= MIN_INT:
                return MIN_INT
        
        return res
        