"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""
import string


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        visited = set()
        worddict = set(wordList)

        queue = [(beginWord, 1)]

        while queue:
            word, count = queue.pop(0)
            if word == endWord:
                return count

            if word in visited:
                continue

            for i, ch in enumerate(word):
                for j in range(26):
                    new_ch = chr(ord('a') + j)
                    if new_ch != ch and word[:i] + new_ch + word[i+1:] in worddict:
                        queue.append((word[:i] + new_ch + word[i+1:], count+1))

            visited.add(word)

        return 0

    def ladderLength2(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict: return 0

        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        wordDict.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = set()
            for w in s1:
                new_words = [
                    w[:i] + t + w[i + 1:] for t in string.ascii_lowercase for i in range(l)]
                for new_word in new_words:
                    if new_word in s2: return step + 1
                    if new_word not in wordDict: continue
                    wordDict.remove(new_word)
                    s.add(new_word)
            s1 = s

        return 0


print(Solution().ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
