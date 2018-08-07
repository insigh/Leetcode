"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        DP = [[False]*(n+1) for i in range(m+1)]
        DP[0][0] = True 
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    DP[i][j] = DP[i][j-2] or (i > 0 and j > 1 and (p[j-2] == '.' or s[i-1] == p[j-2]) and DP[i-1][j])
                elif i > 0 and (p[j-1] == '.' or p[j-1] == s[i-1]):
                    DP[i][j] = DP[i-1][j-1] 
        return DP[m][n]

print(Solution().isMatch("aab", "c*a*b"))