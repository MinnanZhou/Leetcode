class Solution:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        m, n = len(board), len(board[0])
        neighbor = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1]]

        def check(pos, path):
            if board[pos[0]][pos[1]] != "E": return
            possible = []
            count = 0
            for dx, dy in neighbor:
                if 0 <= pos[0] + dx <= m - 1 and 0 <= pos[1] + dy <= n - 1 and (pos[0] + dx, pos[1] + dy) not in path:
                    if board[pos[0] + dx][pos[1] + dy] == "M":
                        count += 1
                    elif board[pos[0] + dx][pos[1] + dy] == "E":
                        possible.append((pos[0] + dx, pos[1] + dy))
            if count:
                board[pos[0]][pos[1]] = str(count)
                return
            for neigh in possible:
                path.add(neigh)
                check(neigh, path)
                path.remove(neigh)
            board[pos[0]][pos[1]] = "B"

        check(click, set(tuple(click)))
        return board


a = Solution()
inp = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]

inp2 = [1, 2]
print(a.updateBoard(inp, inp2))
