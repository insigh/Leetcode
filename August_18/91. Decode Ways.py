"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
"""
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s[0]=='0':
            return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0],dp[1]=1,1
        
        
        
        for i in range(1,len(s)):
            if s[i] =='0':
                if s[i-1]!='1' and s[i-1]!='2':
                    return 0
                else:
                    dp[i+1]=dp[i-1]
            elif int(s[i-1]+s[i])<=26 and s[i-1]!='0':
                dp[i+1]=dp[i]+dp[i-1]
                print(dp)
            else:
                dp[i+1]=dp[i]
        
        return dp[len(s)]