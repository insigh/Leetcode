"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key_value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        s = list(reversed(s))
        res = key_value[s[0]]
        pre_key = s[0]
        for i in range(1,len(s)):
            if key_value[s[i]]<key_value[pre_key]:
                res -= key_value[s[i]]
            else:
                res += key_value[s[i]]
            pre_key = s[i]
        return res
        

