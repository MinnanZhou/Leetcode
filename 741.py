class Solution:
    def cherryPickup(self, grid) -> int:
        prev = {}
        n = len(grid)

        def dp(x1, y1, x2, y2):
            if (x1, y1, x2, y2) in prev: return prev[(x1, y1, x2, y2)]

            if x1 == n or x2 == n or y1 == n or y2 == n: return -1
            if x1 == n - 1 and x2 == n - 1 and y1 == n - 1 and y2 == n - 1: return grid[-1][-1]
            if grid[x1][y1] == -1 or grid[x2][y2] == -1: return -1

            c1 = dp(x1 + 1, y1, x2 + 1, y2)
            c2 = dp(x1, y1 + 1, x2 + 1, y2)
            c3 = dp(x1 + 1, y1, x2, y2 + 1)
            c4 = dp(x1, y1 + 1, x2, y2 + 1)
            output = max(c1, c2, c3, c4)

            if output != -1:
                if x1 == x2 and y1 == y2:
                    output += grid[x1][y1]
                else:
                    output += grid[x1][y1] + grid[x2][y2]

            prev[(x1, y1, x2, y2)] = output
            prev[(x2, y2, x1, y1)] = output
            return output

        return max(dp(0, 0, 0, 0),0)


a = Solution()
inp = [[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1]]
print(a.cherryPickup(inp))
