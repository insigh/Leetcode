"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
"""
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        tries = {}
        for word in words:
            d = tries
            for ch in word:
                if ch not in d:
                    d[ch] = {}
                d = d[ch]
            d[1]=True
        # print(tries)
        M,N = len(board),len(board[0])
        if not M*N:
            return []
        self.res = []
        for i in range(M):
            for j in range(N):
                self.dfs(board,tries,i,j,"")
        return self.res
    
    
    def dfs(self,board,tree,i,j,prefix):
        if 1 in tree and prefix not in self.res:
            self.res.append(prefix)
        
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] not in tree or board[i][j] == "*":
            return 
        
        else:
            tmp = board[i][j]
            board[i][j] = "*"
            self.dfs(board,tree[tmp],i+1,j,prefix+tmp)
                
            self.dfs(board,tree[tmp],i-1,j,prefix+tmp)
                
            self.dfs(board,tree[tmp],i,j-1,prefix+tmp)
                
            self.dfs(board,tree[tmp],i,j+1,prefix+tmp)
                
            board[i][j] = tmp
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            