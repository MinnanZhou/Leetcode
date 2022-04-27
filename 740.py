from collections import Counter
from functools import cache


class Solution:
    def deleteAndEarn(self, nums) -> int:
        remain = Counter(nums)
        values = sorted(list(remain.items()), key=lambda x: x[0])

        @cache
        def dp(i):
            if i >= len(values):
                return 0
            if i == len(values) - 1:
                return values[i][0] * values[i][1]
            if values[i][0] + 1 == values[i + 1][0]:
                return max(dp(i + 2) + values[i][0] * values[i][1], dp(i + 1))
            else:
                return dp(i + 1) + values[i][0] * values[i][1]

        return dp(0)


a = Solution()
inp = [3, 3, 3, 4, 2]
print(a.deleteAndEarn(inp))
