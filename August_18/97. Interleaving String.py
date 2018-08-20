"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.cache = {}
        return self.docheck(s1,s2,s3)
        
    def docheck(self,s1,s2,s3):
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l3 != l1+l2:
            self.cache[(s1,s2,s3)] = False
            return False
        if (s1,s2,s3) in self.cache and self.cache[(s1,s2,s3)]:
            return True
        if (s1,s2,s3) in self.cache and not self.cache[(s1,s2,s3)]:
            return False
        elif s1 == s3 :
            self.cache[(s1,s2,s3)] = True
            return True
        elif s3 == s2:
            self.cache[(s1,s2,s3)] = True
            return True
        elif s1 and s3[0] == s1[0]:
            if self.docheck(s1[1:],s2,s3[1:]):
                self.cache[(s1,s2,s3)] = True
                return True
            
        if s2 and s3[0] == s2[0]:
            
            if self.docheck(s1,s2[1:],s3[1:]):
                self.cache[(s1,s2,s3)] = True
                return True
        self.cache[(s1,s2,s3)] = False  
        return False
        