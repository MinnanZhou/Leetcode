from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        nodemat = [[0 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    if i == 0 and j == 0:
                        nodemat[i][j] = 1
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

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1: return 0
        matrix = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        matrix[-1][-1] = 1
        for i in range(len(obstacleGrid) - 1, -1, -1):
            for j in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[i][j] == 1: continue
                right = matrix[i][j + 1] if j + 1 < len(obstacleGrid[i]) else 0
                bottom = matrix[i + 1][j] if i + 1 < len(obstacleGrid) else 0
                matrix[i][j] += right + bottom
        return matrix[0][0]


a = Solution()
inp = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(a.uniquePathsWithObstacles2(inp))
