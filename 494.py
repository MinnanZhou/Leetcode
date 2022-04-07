from functools import cache


class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        @cache
        def dp(i, remain):
            if i < 0 and remain == 0:
                return 1
            if i < 0:
                return 0
            return dp(i - 1, remain - nums[i]) + dp(i - 1, remain + nums[i])

        return dp(len(nums) - 1, target)


a = Solution()
inp = [27,33,4,43,31,44,47,6,6,11,39,37,15,16,8,19,48,17,18,39]
print(a.findTargetSumWays(inp, 24))
