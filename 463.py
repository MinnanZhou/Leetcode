class Solution:
    def islandPerimeter(self, grid) -> int:
        peri = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = 4
                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == 1:
                            count -= 1
                    peri += count
        return peri
