class Solution:
    def getRow(self, rowIndex: int):
        res = [1]
        for i in range(1, rowIndex):
            nextline = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    nextline.append(1)
                else:
                    nextline.append(res[j - 1] + res[j])
            res = nextline
        return res


a = Solution()
print(a.getRow(6))
