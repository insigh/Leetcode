"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        visited = {0, }
        queue = [(0, 0)]
        while queue:
            cut, idx = queue.pop(0)
            if s[idx:] == s[idx:][::-1]: return cut
            for i in range(idx + 1, len(s)):
                if i not in visited and s[idx: i] == s[idx: i][::-1]:
                    visited.add(i)
                    queue.append((cut + 1, i))
