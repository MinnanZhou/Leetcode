import heapq


class Solution:
    def trapRainWater(self, heightMap) -> int:
        m, n = len(heightMap), len(heightMap[0])
        hp = []
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    hp.append((heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        heapq.heapify(hp)
        res, level = 0, 0
        while hp:
            h, x, y = heapq.heappop(hp)
            level = max(level, h)
            res += (level - h)
            for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                new = (x + dx, y + dy)
                if 0 <= new[1] < n and 0 <= new[0] < m and heightMap[new[0]][new[1]] != -1:
                    heapq.heappush(hp, (heightMap[new[0]][new[1]], new[0], new[1]))
                    heightMap[new[0]][new[1]] = -1
        return res


a = Solution()
inp = [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]
print(a.trapRainWater(inp))
