"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row, col, res = len(board), len(board[0]), set()
        for i in range(row):
            self.dfs(i, 0, res, board)
            self.dfs(i, col - 1, res, board)
        for j in range(col):
            self.dfs(0, j, res, board)
            self.dfs(row - 1, j, res, board)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i, j) not in res:
                    board[i][j] = 'X'

    def dfs(self, i, j, res, board):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == 'X' or (i, j) in res:
            return

        elif board[i][j] == 'O':
            res.add((i, j))
            self.dfs(i + 1, j, res, board)
            self.dfs(i - 1, j, res, board)
            self.dfs(i, j - 1, res, board)
            self.dfs(i, j + 1, res, board)


