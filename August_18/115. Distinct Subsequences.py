"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
"""
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        self.cache = {}
        count = self.findAllsubsequence(s, t)
        
        return count 
    
    
    def findAllsubsequence(self, s, t):
        
        if (s, t) in self.cache:
            return self.cache[(s, t)]
        
        count = 0
        if len(t) == 1:
            # c = collections.Counter(s)
            # count = collections.Counter(s)[t]
            count = 0 
            for i in range(len(s)):
                if s[i] == t:
                    count += 1
            self.cache[(s, t)] = count 
            return count 
        
        for i in range(len(s)):
            if s[i] == t[0]:
                count += self.findAllsubsequence(s[i+1:], t[1:])
        self.cache[(s, t)] = count 
        return count 
        
