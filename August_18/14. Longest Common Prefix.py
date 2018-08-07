"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min (strs,key =len)
        for i,ch in enumerate(shortest):
            for str_ in strs:
                if str_[i] != ch:
                    return shortest[:i]
        return shortest
print(Solution().longestCommonPrefix(["flower","flow","flight"]))