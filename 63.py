class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        nodemat = [[0 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    if i==0 and j==0:
                        nodemat[i][j]=1
                    if i == 0:
                        up = 0
                    else:
                        up = nodemat[i - 1][j]
                    if j == 0:
                        left = 0
                    else:
                        left = nodemat[i][j - 1]
                    nodemat[i][j] += left + up
        return nodemat[-1][-1]


a = Solution()
inp = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(a.uniquePathsWithObstacles(inp))
