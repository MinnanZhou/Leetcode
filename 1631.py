import random


class Solution:
    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        neighbor = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def getMinMax(matrix):
            minDiff, maxDiff = float('inf'), float('-inf')
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    for dx, dy in neighbor:
                        if 0 <= i + dx < m and 0 <= j + dy < n:
                            minDiff = min(minDiff, abs(heights[i + dx][j + dy] - heights[i][j]))
                            maxDiff = max(maxDiff, abs(heights[i + dx][j + dy] - heights[i][j]))
            if minDiff == float('inf'):
                return 0, 0
            else:
                return minDiff, maxDiff

        def check(val, path, x=0, y=0):
            path.add((x,y))
            if x == m - 1 and y == n - 1:
                return True
            ret = False
            for dx, dy in neighbor:
                if 0 <= x + dx < m and 0 <= y + dy < n and (x + dx, y + dy) not in path:
                    if abs(heights[x + dx][y + dy] - heights[x][y]) <= val:
                        if check(val, path, x + dx, y + dy):
                            return True
            return ret

        l, r = 0, 100000
        while l < r:
            mid = (l + r) // 2
            if check(mid, {(0,0)}):
                r = mid
            else:
                l = mid + 1
        return l


a = Solution()
inp = [[random.randint(0, 100000) for _ in range(20)] for _ in range(20)]
print(a.minimumEffortPath(inp))
