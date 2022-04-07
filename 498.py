class Solution:
    def findDiagonalOrder(self, mat):
        direction = 0
        start = [0, 0]
        ret = [mat[0][0]]
        count = len(mat) * len(mat[0])
        while len(ret) < count:
            if direction == 0:
                if start[1] < len(mat[0]) - 1:
                    start[1] += 1
                else:
                    start[0] += 1
                while start[1] >= 0 and start[0] < len(mat):
                    ret.append(mat[start[0]][start[1]])
                    start[1] -= 1
                    start[0] += 1
                start[1] += 1
                start[0] -= 1
                direction = 1
            else:
                if start[0] < len(mat) - 1:
                    start[0] += 1
                else:
                    start[1] += 1
                while start[0] >= 0 and start[1] < len(mat[0]):
                    ret.append(mat[start[0]][start[1]])
                    start[1] += 1
                    start[0] -= 1
                start[1] -= 1
                start[0] += 1
                direction = 0
        return ret


a = Solution()
inp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a.findDiagonalOrder(inp))
