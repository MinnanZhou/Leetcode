from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def count(i, j):
            if i >= len(s) or j >= len(t):
                return 0
            if s[i] == t[j]:
                if j == len(t) - 1:
                    return 1 + count(i + 1, j)
                x = count(i + 1, j + 1) + count(i + 1, j)
                return x
            x = count(i + 1, j)
            return x

        return count(0, 0)


a = Solution()
inp1 = "babgbag"
inp2 = "bag"
print(a.numDistinct(inp1, inp2))
