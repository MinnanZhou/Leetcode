class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        def count(pos: tuple, area: set):
            if grid[pos[0]][pos[1]] > 0 and pos not in area:
                area.add(pos)
                grid[pos[0]][pos[1]] = 0
                if pos[0] + 1 < m: count((pos[0] + 1, pos[1]), area)
                if pos[0] - 1 >= 0: count((pos[0] - 1, pos[1]), area)
                if pos[1] + 1 < n: count((pos[0], pos[1] + 1), area)
                if pos[1] - 1 >= 0: count((pos[0], pos[1] - 1), area)
            return len(area)

        ret = 0
        m, n = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret = max(ret, count((i, j), set()))
        return ret


a = Solution()
inp = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(a.maxAreaOfIsland(inp))
