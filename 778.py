class Solution:
    def swimInWater(self, grid) -> int:
        def findPath(th, path, i=0, j=0):
            if grid[i][j] > th:
                return False
            if i == n - 1 and j == m - 1:
                return True
            path.add((i, j))
            for dx, dy in neighbor:
                if 0 <= i + dx < m and 0 <= j + dy < n and (i + dx, j + dy) not in path:
                    if findPath(th, path, i + dx, j + dy): return True
            return False

        neighbor = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        l, r = grid[-1][-1], max([max(row) for row in grid])
        while l <= r:
            mid = (l + r) // 2
            if not findPath(mid, set()):
                l = mid + 1
            else:
                r = mid - 1
        return l


a = Solution()
inp = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
print(a.swimInWater(inp))
