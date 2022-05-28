from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(k):
            if k < 0:
                return 0
            if k <= 1:
                return 1
            return dp(k - 1) + dp(k - 2)

        return dp(n)


a = Solution()
print(a.climbStairs(30))
