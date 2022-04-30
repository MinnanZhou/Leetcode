import collections


class Solution:
    def movesToChessboard(self, board) -> int:
        n = len(board)
        if n <= 1:
            return 0
        rows = [''.join(str(c) for c in r) for r in board]
        counter = collections.Counter(rows)
        keys = list(counter)
        if len(keys) != 2 or abs(counter[keys[0]] - counter[keys[1]]) > 1 \
                or abs(keys[0].count('1') - keys[0].count('0')) > 1 \
                or any(a == b for a, b in zip(*keys)):
            return -1
        rd, cd = 0, 0
        for i in range(n):
            rd += board[0][i] == i % 2
            cd += board[i][0] == i % 2
        if n % 2 == 0:
            rd = min(rd, n - rd)
        elif rd % 2 != 0:
            rd = n - rd
        if n % 2 == 0:
            cd = min(cd, n - cd)
        elif cd % 2 != 0:
            cd = n - cd
        return (rd + cd) // 2


a = Solution()
inp = [[1, 1, 0], [0, 0, 1], [0, 0, 1]]
print(a.movesToChessboard(inp))
