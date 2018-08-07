"""
Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
         
        key_value = {'I':1, 'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        key_value = {value:key for key,value in key_value.items()}
        reversed_key_sorted = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        dp = ['']*(num+1)
        for i in range(num+1):
            for j in reversed_key_sorted:
                if i>=j:
                    dp[i] = key_value[j]+dp[i-j]
                    break
                    
        return dp[num]

class Solution1:
    
    ONE = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    TEN = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    HUN = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    THU = ["", "M", "MM", "MMM"]
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return Solution1.THU[num // 1000 % 10] + Solution1.HUN[num // 100 % 10] + Solution1.TEN[num // 10 % 10] + Solution1.ONE[num % 10];