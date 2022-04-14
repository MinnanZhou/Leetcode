import math


class Solution:
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        ret = [[0 for _ in range(n)] for _ in range(m)]
        neighbor = [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1]]
        for i in range(m):
            for j in range(n):
                s, c = 0, 0
                for dx, dy in neighbor:
                    if 0 <= i + dx <= m - 1 and 0 <= j + dy <= n - 1:
                        s += img[i + dx][j + dy]
                        c += 1
                ret[i][j] = math.floor(s / c)

        return ret


a = Solution()
inp = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
print(a.imageSmoother(inp))
