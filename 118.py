class Solution:
    def generate(self, numRows: int):
        res = [[1]]
        for i in range(1, numRows):
            nextline = []
            for j in range(i+1):
                if j == 0 or j == i:
                    nextline.append(1)
                else:
                    nextline.append(res[-1][j - 1] + res[-1][j])
            res.append(nextline)
        return res


a = Solution()
print(a.generate(30))
