class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] += dp[j - i]

        return dp[-1]


a = Solution()
inp = 12
inp2 = [1, 2, 5]
print(a.change(inp, inp2))
