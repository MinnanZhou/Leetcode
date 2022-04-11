class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        if r * c != len(mat) * len(mat[0]): return mat
        ret = []
        row = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row.append(mat[i][j])
                if len(row) == c:
                    ret.append(row)
                    row = []
        return ret


a = Solution()
inp = [[1, 2], [3, 4]]
print(a.matrixReshape(inp, 1, 4))
