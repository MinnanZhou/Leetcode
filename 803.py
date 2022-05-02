class Solution:
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            return sum([dfs(i + 1, j), dfs(i, j + 1), dfs(i - 1, j), dfs(i, j - 1)]) + 1

        def connect(i, j):
            return i == 0 or any([0 <= x < m and 0 <= y < n and grid[x][y] == 2 for x, y in
                                  [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]])

        for x, y in hits:
            grid[x][y] -= 1

        for x in range(n):
            if grid[0][x]:
                dfs(0, x)

        h = len(hits)
        ret = [0 for _ in range(h)]
        for i, (x, y) in enumerate(hits[::-1]):
            grid[x][y] += 1
            if grid[x][y] > 0 and connect(x, y):
                ret[h - 1 - i] = dfs(x, y) - 1
        return ret


a = Solution()
inp = [[1,0,1],[0,0,1]]

inp2 = [[1,0],[0,0]]
print(a.hitBricks(inp, inp2))
