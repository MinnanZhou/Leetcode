class Solution:
    def candy(self, ratings) -> int:
        candies = [0 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 1, 1, -1):
            if ratings[i - 2] >= ratings[i - 1] > ratings[i]:
                candies[i - 1] = candies[i] + 1
            elif ratings[i - 1] > ratings[i - 2] and ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i], candies[i - 2]) + 1
        if len(candies) >= 2:
            candies[0] = candies[1] + 1 if ratings[0] > ratings[1] else 0
            candies[-1] = candies[-2] + 1 if ratings[-1] > ratings[-2] else 0
        return sum(candies) + len(ratings) * (1 - min(candies))


a = Solution()
inp1 = [1, 0, 2]
print(a.candy(inp1))
