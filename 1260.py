class Solution:
    def shiftGrid(self, grid, k: int):
        flatten = []
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        for row in grid:
            flatten += row
        flatten = flatten[-k:] + flatten[:-k]
        flatten = [flatten[k * n:(k + 1) * n] for k in range(m)]
        return flatten


a = Solution()
inp = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
inp2 = 23
print(a.shiftGrid(inp, inp2))
