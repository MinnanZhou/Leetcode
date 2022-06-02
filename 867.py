class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        newMat = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                newMat[j][i] = matrix[i][j]
        return newMat
