class Solution:
    def countBattleships(self, board) -> int:
        count = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    count += 1
                    board[i][j] = -1
                    for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        start = [i, j]
                        while 0 <= start[0] + direction[0] <= m - 1 and 0 <= start[1] + direction[1] <= n - 1 and \
                                board[start[0] + direction[0]][start[1] + direction[1]] == 'X':
                            board[start[0] + direction[0]][start[1] + direction[1]] = -1
                            start[0], start[1] = start[0] + direction[0], start[1] + direction[1]
        return count


a = Solution()
inp = [[".", "X", ".", ".", "X"],
       [".", "X", ".", ".", "X"],
       [".", ".", ".", ".", "X"],
       ["X", ".", "X", "X", "."],
       ["X", ".", ".", ".", "X"]]
print(a.countBattleships(inp))
