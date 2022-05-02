class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        EMax = [max(row) for row in grid]
        NMax = [max([row[i] for row in grid]) for i in range(len(grid[0]))]
        total = sum(sum(row) for row in grid)
        for i in EMax:
            for j in NMax:
                total -= min(i, j)
        return -total


a = Solution()
inp = [[3, 0, 8, 4],
       [2, 4, 5, 7],
       [9, 2, 6, 3],
       [0, 3, 1, 0]]
print(a.maxIncreaseKeepingSkyline(inp))
