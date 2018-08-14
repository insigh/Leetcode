"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'""" 
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        L1,L2 = len(word1),len(word2)
        dp = [[0 for j in range(L1+1)] for j in range(L2+1)]
        for i in range(L2+1):
            for j in range(L1+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0 and j > 0:
                    dp[i][j] = j
                elif j==0 and i > 0:
                    dp[i][j] = i
                else:
                    if word1[j-1]==word2[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        # print(dp)
        return dp[-1][-1]
        
                    
                    