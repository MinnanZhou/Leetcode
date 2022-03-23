class Solution:
    def maxProfit(self, prices):
        one_buy = two_buy = float('inf')
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)
        return two_profit


a = Solution()
inp2 = [6, 1, 3, 2, 6, 4,7]
print(a.maxProfit(inp2))
