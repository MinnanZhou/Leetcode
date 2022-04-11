class Solution:
    def updateMatrix(self, mat):
        neighbor = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(mat), len(mat[0])
        start = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: start.add((i, j))
                if mat[i][j] == 1: mat[i][j] = 'X'
        i = 1
        while start:
            next_set = set()
            for pos in start:
                for dx, dy in neighbor:
                    if 0 <= pos[0] + dx < m and 0 <= pos[1] + dy < n and mat[pos[0] + dx][pos[1] + dy]=='X':
                        mat[pos[0] + dx][pos[1] + dy] = i
                        next_set.add((pos[0] + dx, pos[1] + dy))
            start = next_set
            i += 1
        return mat


a = Solution()
inp = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
       [1, 1, 1, 0, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
       [1, 0, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
       [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]]
print(a.updateMatrix(inp))
x = [[inp[i][j] for j in range(6)] for i in range(5)]
