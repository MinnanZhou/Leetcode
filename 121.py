class Solution:
    def maxProfit(self, prices) -> int:
        res = 0
        maxPrice = prices[-1]
        for i in range(len(prices) - 1):
            if prices[-i-1]>prices[-i-2]:
                maxPrice = max(maxPrice, prices[-1 - i])
                res = max(res, maxPrice - prices[-2 - i])
        return res


a = Solution()
inp = [7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1,
       5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4]
print(a.maxProfit(inp))
