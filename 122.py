class Solution:
    def maxProfit(self, prices) -> int:
        prices.append(0)
        total_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                total_profit += max(0, prices[i - 1] - buy)
                buy = prices[i]
        return total_profit


a = Solution()
inp = [6,1,3,2,4,7]
print(a.maxProfit(inp))
