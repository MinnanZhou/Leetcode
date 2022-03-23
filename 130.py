class Solution:
    def solve(self, board) -> None:
        out = [[0, i] for i in range(len(board[0]))] + [[len(board) - 1, i] for i in range(len(board[0]))]
        out += [[i, 0] for i in range(1, len(board) - 1)] + [[i, len(board[0]) - 1] for i in range(1, len(board) - 1)]
        for x, y in out:
            while board[x][y] == 'O':
                self.func(board, x, y)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'

    def func(self, board, x, y):
        if 0 <= x <= len(board) - 1 and 0 <= y <= len(board[0]) - 1:
            if board[x][y] == 'O':
                board[x][y] = 'Y'
                self.func(board, x + 1, y)
                self.func(board, x - 1, y)
                self.func(board, x, y + 1)
                self.func(board, x, y - 1)


a = Solution()
inp = [['X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X'], ['X', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'X'],
       ['O', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'O'],
       ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'O'], ['O', 'O', 'X', 'X', 'O', 'X', 'O', 'O', 'X', 'X']]
print(a.solve(inp))
