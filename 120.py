class Solution:
    def minimumTotal(self, triangle) -> int:
        prevpath = [triangle[0][0]]
        for i in range(1, len(triangle)):
            path = []
            for j in range(i + 1):
                if j == 0:
                    path.append(prevpath[j] + triangle[i][j])
                elif j == i:
                    path.append(prevpath[j - 1] + triangle[i][j])
                else:
                    path.append(min(prevpath[j], prevpath[j - 1]) + triangle[i][j])
            prevpath = path
        return min(prevpath)


a = Solution()
inp = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
x = a.minimumTotal(inp)
print(x)
