class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        neighbor = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        prev = image[sr][sc]
        if prev == newColor: return image
        m, n = len(image), len(image[0])

        def change(x, y):
            if image[x][y] == prev:
                image[x][y] = newColor
                for dx, dy in neighbor:
                    if 0 <= x + dx <= m - 1 and 0 <= y + dy <= n - 1:
                        change(x + dx, y + dy)

        change(sr, sc)
        return image


a = Solution()
inp = [[0, 0, 0], [0, 1, 1]]
print(a.floodFill(inp, 1, 1, 1))
