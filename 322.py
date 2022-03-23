class Solution:
    def coinChange(self, coins, amount: int):
        a = [float('inf') for _ in range(amount + 1)]
        a[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    a[i] = min(a[i], a[i - coin] + 1)
        return a[-1] if a[-1] != float('inf') else -1


a = Solution()
print(a.coinChange([1,2,5], 100))
