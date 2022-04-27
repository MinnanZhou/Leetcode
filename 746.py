from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        @cache
        def dp(i):
            if i >= len(cost):
                return 0
            return min(dp(i + 1), dp(i + 2)) + cost[i]

        return min(dp(0), dp(1))
