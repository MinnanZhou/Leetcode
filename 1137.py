class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1] + [0 for _ in range(n - 2)]
        for i in range(3, n + 1):
            dp[i] = sum(dp[i - 3:i])
        return dp[n]


a = Solution()
print(a.tribonacci(6))
