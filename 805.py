from functools import lru_cache


class Solution:
    def splitArraySameAverage(self, nums) -> bool:
        total = sum(nums)
        n = len(nums)

        @lru_cache
        def dp(i, k, s):
            if k == 0: return s == 0
            if k + i >= n or s < 0: return False
            return dp(i + 1, k, s) or dp(i + 1, k - 1, s - nums[i])

        for j in range(1, n//2 + 1):
            if total * j % n == 0 and dp(0, j, total * j // n):
                return True
        return False


a = Solution()
inp = [0, 13, 13, 7, 5, 0, 10, 19, 5]
print(a.splitArraySameAverage(inp))
