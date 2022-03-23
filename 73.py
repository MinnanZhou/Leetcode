class Solution:
    def setZeroes(self, matrix) -> None:
        col=[]
        row=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    col.append(j)
                    row.append(i)
        col=list(set(col))
        row=list(set(row))
        for k in row:
            for m in range(len(matrix[0])):
                matrix[k][m]=0
        for k in col:
            for m in range(len(matrix)):
                matrix[m][k]=0


a=Solution()
inp=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
a.setZeroes(inp)