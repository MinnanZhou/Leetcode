class Solution:
    def orderOfLargestPlusSign(self, n: int, mines) -> int:
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
        for m in mines: matrix[m[0]][m[1]] = 0
        for i in range(n):
            l, r, u, d = 0, 0, 0, 0
            for j in range(n):
                l = l + 1 if matrix[i][j] != 0 else 0
                r = r + 1 if matrix[i][n - 1 - j] != 0 else 0
                matrix[i][j] = min(l, matrix[i][j])
                matrix[i][n - 1 - j] = min(r, matrix[i][n - 1 - j])
                u = u + 1 if matrix[j][i] != 0 else 0
                d = d + 1 if matrix[n - 1 - j][i] != 0 else 0
                matrix[j][i] = min(u, matrix[j][i])
                matrix[n - 1 - j][i] = min(d, matrix[n - 1 - j][i])
        return int(max([max(row) for row in matrix]))


a = Solution()
inp = 2

inp2 = [[0,0],[0,1],[1,0]]
print(a.orderOfLargestPlusSign(inp, inp2))
