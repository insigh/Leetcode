"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        N,res = len(strs),[]
        strs_sort = {i:("".join((lambda x:(x.sort(),x)[1])(list(s)))) for i,s in enumerate(strs)}
        strs_sorted = sorted(strs_sort.items(),key=lambda x:x[1])
        
        print(strs_sorted)
        
        res.append([strs[strs_sorted[0][0]]])
        temp = strs_sorted[0][1]
        
        for i in range(1,N):
            if strs_sorted[i][1]==strs_sorted[i-1][1]:
                res[-1].append(strs[strs_sorted[i][0]])
            else:
                temp = strs_sorted[i][1]
                res.append([strs[strs_sorted[i][0]]])
        return res
            
        