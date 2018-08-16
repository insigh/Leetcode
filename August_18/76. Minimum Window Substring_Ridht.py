"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needs,missing = collections.Counter(t),len(t)
        i=I=J=0
        for j,h in enumerate(s,1):
            missing -= needs[h]>0
            needs[h] -= 1
            if not missing:
                while needs[s[i]]<0:
                    needs[s[i]] += 1
                    i += 1
                if not J or j-i<J-I:
                    I,J = i,j
        return s[I:J]

        
        
        