"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
 
        if p =="*":
            pass
        else:
            p=list(p)
            d =[]      
            for item in p:
                if item !="*" or len(d)<1 or (item=="*" and len(d)>=1 and d[-1]!='*'):
                    # print(item)
                    d.append(item)
            p = "".join(d)
        # print(p)
        dp = [[False for _ in range(len(s)+1)] for item in range(len(p)+1)]
        # print(dp)
        S= len(s)
        P= len(p)
        # dp[0][0]=True
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i ==0 and j==0:
                    dp[i][j]=True
                elif i==0 and j!=0:
                    dp[i][j]=False
                elif j==0 and i!=0:
                    dp[i][j] = ( p[i-1]=='*' and dp[i-1][0])
                    
                else:   
                    if p[i-1]==s[j-1] or p[i-1]=='?':
                        dp[i][j]=dp[i-1][j-1]

                    elif p[i-1]=='*':
                        dp[i][j]=(dp[i-1][j] or dp[i][j-1])
        # print(dp)
                 
        return dp[P][S]
    
    
        
                
        
        