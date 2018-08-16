"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        list1 = [ ord(x)-ord('a') for x in s1]
        list2 = [ ord(x)-ord('a') for x in s2]
        target = [0]*26
        for x in (list1):
            target[x] += 1
        # print(target)
        window = [0]*26
        for j,ch in enumerate(list2):
            window[ch] += 1
            # print(window)
            if j >= len(list1):
                window[list2[j-len(list1)]] -= 1
            if window==target:
                return True
        return False
        