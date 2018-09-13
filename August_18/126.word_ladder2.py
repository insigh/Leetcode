"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
"""
import string
import collections


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        # for word in wordList:
        #     wordSet.add(word)

        level = set([beginWord])

        parents = collections.defaultdict(set)

        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for i in range(len(beginWord)):
                    p1 = word[:i]
                    p2 = word[i + 1:]
                    for j in string.ascii_lowercase:
                        # accelerate
                        if word[i] != j:
                            childWord = p1 + j + p2
                            if childWord in wordSet and childWord not in parents:
                                next_level[childWord].add(word)
            level = next_level
            parents.update(next_level)
        print(parents)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]

        return res


print(Solution().findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))