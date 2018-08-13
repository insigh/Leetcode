"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)
        res =""
        for i in range(L-1,-1,-1):
            res += s[i]
        return res
        