"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        else:
            res = []
            for i in range(len(s)):
                temp = s[i:]
                if temp == temp[::-1]:
                    for term in self.partition(s[:i]):
                        res.append(term+[temp] )
        return res