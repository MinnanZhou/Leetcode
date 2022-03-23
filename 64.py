class Solution:
    def minPathSum(self, grid) -> int:
        nodemat = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    nodemat[i][j] = grid[i][j]
                elif i == 0:
                    nodemat[i][j] = grid[i][j] + nodemat[i][j-1]
                elif j == 0:
                    nodemat[i][j] = grid[i][j] + nodemat[i-1][j]
                else:
                    nodemat[i][j] = grid[i][j] + min(nodemat[i][j-1], nodemat[i-1][j])
        return nodemat[-1][-1]


a = Solution()
inp = [[1,3,1],[1,5,1],[4,2,1]]
print(a.minPathSum(inp))
