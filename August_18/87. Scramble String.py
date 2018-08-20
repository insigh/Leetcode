"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
"""
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.cache = {}
        return self.docheck(s1,s2)
    
    def docheck(self,s1,s2):
        if s1 == s2:
            self.cache[(s1,s2)] = True
            return True
        if (s1,s2) in self.cache.keys() and self.cache[(s1,s2)] :
            return True
        
        ls =[0]*26
        len_ = len(s1)
        for i in range(len_):
            ls[ord(s1[i])-ord('a')] += 1
            ls[ord(s2[i])-ord('a')] -= 1
            
        for i in range(26):
            if ls[i] != 0:
                self.cache[(s1,s2)] = False
                return False
            
        for i in range(1,len_):
            if self.docheck(s1[:i],s2[:i]) and self.docheck(s1[i:],s2[i:]):
                self.cache[(s1,s2)] = True
                return True
            if self.docheck(s1[:i],s2[len_-i:]) and self.docheck(s1[i:],s2[:len_-i]):
                self.cache[(s1,s2)] = True
                return True     
        self.cache[(s1,s2)] = False
        return False