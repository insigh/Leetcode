""" 
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        res = ""
        max_length = 0
        for i in range(len(s)):
            temp = self.striver(s,i,i)
            if len(temp) > max_length :
                max_length = len(temp)
                res = temp
            temp = self.striver(s,i,i+1)
            if len(temp) > max_length :
                max_length = len(temp)
                res = temp
        return res
        
    def striver(self,s,l,r):
        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            l -= 1 ; r += 1
        
        return s[l+1:r]

print(Solution().longestPalindrome("babad"))