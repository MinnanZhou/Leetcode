class Solution:
    def exist(self, board, word: str) -> bool:
        for i in board:
            i.insert(0, 0)
            i.append(0)
        board = [[0 for i in range(len(board[0]))]] + board + [[0 for i in range(len(board[0]))]]
        start = []
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if word[0] == board[i][j]:
                    start.append([i, j])
        for i in start:
            if self.search(board, word, i, 1, [i]):
                return True
        return False

    def search(self, board, word, position, letter, path):
        if letter == len(word):
            return True
        else:
            for i in [[position[0], position[1] + 1], [position[0], position[1] - 1], [position[0] + 1, position[1]], [position[0] - 1, position[1]]]:
                if board[i[0]][i[1]] == word[letter] and i not in path:
                    if self.search(board, word, i, letter + 1, path+[i]):
                        return True
            return False


a = Solution()
inp1 = [["C","A","A"],["A","A","A"],["B","C","D"]]
inp2 = 'CBD'
print(a.exist(inp1, inp2))
