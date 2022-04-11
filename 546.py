from functools import lru_cache, cache


class Solution:
    def removeBoxes(self, boxes) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            if i > j: return 0
            indx = [m for m in range(i + 1, j + 1) if boxes[m] == boxes[i]]
            ans = (k + 1) ** 2 + dp(i + 1, j, 0)
            return max([ans] + [dp(i + 1, m - 1, 0) + dp(m, j, k + 1) for m in indx])

        return dp(0, len(boxes) - 1, 0)


a = Solution()
inp = [4, 5, 5, 5, 4, 3, 5, 4, 4, 3, 4, 4, 4, 4, 3, 5, 5, 4, 5]
print(a.removeBoxes(inp))
