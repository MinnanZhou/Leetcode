class Solution:
    def numIslands(self, grid) -> int:
        island = 0
        for i in range(len(grid)):
            grid[i].insert(0, "0")
            grid[i].append("0")
        grid.insert(0, ["0" for _ in range(len(grid[0]))])
        grid.append(["0" for _ in range(len(grid[0]))])
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == "1":

                    def recur(x, y):
                        if grid[x][y] == "1":
                            grid[x][y] = "2"
                            recur(x + 1, y)
                            recur(x - 1, y)
                            recur(x, y + 1)
                            recur(x, y - 1)

                    recur(i, j)
                    island += 1
        return island


a = Solution()
inp = [
    ["1", "1", "0", "1"],
    ["1", "1", "0", "1",],
    ["0", "0", "1", "0",],
    ["1", "0", "0", "0",]]
inp2=[["1"]]
print(a.numIslands(inp2))
