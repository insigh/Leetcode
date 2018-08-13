"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
"""
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','o','e','i','u','A','O','E','I','U']
        s = list(s)
        i = 0
        j = len(s)-1
        
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j] = s[j],s[i]
                i+=1;j-=1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
        return ''.join(s)
                
        
        