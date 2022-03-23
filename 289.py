class Solution:
    def gameOfLife(self, board) -> None:
        m = len(board)
        n = len(board[0])
        ajc = [[1, 0], [0, 1], [1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [-1, 1]]
        for i in range(m):
            board[i].append(0)
            board[i].insert(0, 0)
        board.append([0 for _ in range(n + 2)])
        board.insert(0, [0 for _ in range(n + 2)])
        for i in range(m + 2):
            for j in range(n + 2):
                if board[i][j] >= 1:
                    for x, y in ajc:
                        if 0 <= i + x <= m + 1 and 0 <= j + y <= n + 1 and board[i + x][j + y] >= 1:
                            board[i + x][j + y] += 1
                else:
                    for x, y in ajc:
                        if 0 <= i + x <= m + 1 and 0 <= j + y <= n + 1 and board[i + x][j + y] <= 0:
                            board[i + x][j + y] -= 1
        del board[0], board[-1]
        for i in range(m):
            del board[i][0], board[i][-1]
            for j in range(n):
                if 3 <= board[i][j] <= 4 or board[i][j] == -5:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        return board


a = Solution()
inp = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(a.gameOfLife(inp))
