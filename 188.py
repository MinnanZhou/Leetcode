class Solution:
    def maxProfit(self, prices, k):
        buy = [float('inf') for _ in range(k)]
        profit = [0 for _ in range(k)]
        profit.insert(0, 0)
        for p in prices:
            for i in range(k):
                buy[i] = min(buy[i], p - profit[i])
                profit[i+1] = max(profit[i + 1], p - buy[i])
        return profit[-1]


a = Solution()
inp2 = [6, 1, 3, 2, 6, 4, 7]
print(a.maxProfit(inp2, 4))
