"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        M,N = len(board),len(board[0])
        if M*N==0:
            return False
        for i in range(M):
            for j in range(N):
                if self.dfs(board,word,i,j):
                    return True
        return False
                
    def dfs(self,board,word,i,j):
        if len(word)==0:
            return True
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        else:
            tmp = board[i][j]
            board[i][j] = "*"
            res = self.dfs(board,word[1:],i+1,j) or self.dfs(board,word[1:],i-1,j) \
                  or self.dfs(board,word[1:],i,j-1) or self.dfs(board,word[1:],i,j+1)
            board[i][j] = tmp
            return res