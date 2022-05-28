class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        grid = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        grid[0] = [i for i in range(len(word1) + 1)]
        for j in range(len(word2) + 1):
            grid[j][0] = j
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                grid[i][j] = min(grid[i - 1][j - 1] + (1 if word2[i - 1] != word1[j - 1] else 0), grid[i][j - 1]+1,
                                 grid[i - 1][j]+1)
        return grid[-1][-1]


a = Solution()
inp = "horse"
inp2 = "ros"
print(a.minDistance(inp, inp2))
