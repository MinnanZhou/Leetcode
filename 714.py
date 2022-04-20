class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        cost = prices[0]
        maxPrice = prices[0]
        profit = 0
        for price in prices[1:]:
            if price + fee >= maxPrice:
                if price < cost:
                    cost = price
                    maxPrice = price
                maxPrice = max(maxPrice, price)
                continue
            else:
                profit += max(maxPrice - cost - fee, 0)
                cost = price
                maxPrice = price
        return profit + max(maxPrice - cost - fee, 0)


a = Solution()
inp = [1,3,7,5,10,3]
print(a.maxProfit(inp, 3))
