class NumMatrix:

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.sum = [[0] for _ in range(m+1)]
        for j in range(n):
            self.sum[0].append(0)

        for i in range(len(matrix)):
            for j in range(n):
                self.sum[i+1].append(self.sum[i+1][-1] + matrix[i][j]+self.sum[i][j+1]-self.sum[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum[row2+1][col2+1]-self.sum[row2+1][col1]-self.sum[row1][col2+1]+self.sum[row1][col1]


inp = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
a = NumMatrix(inp)
print(a.sumRegion(0, 0, 4, 4))
