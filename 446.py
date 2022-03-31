from collections import Counter


class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        n = len(nums)
        total = 0
        stat = [Counter() for _ in range(n)]
        for i in range(n):
            for j in range(i):
                stat[i][nums[i] - nums[j]] += (stat[j][nums[i] - nums[j]] + 1)
            total += sum(stat[i].values())
        return total - n * (n - 1) // 2


a = Solution()
inp = [2, 4, 6, 8, 10]
print(a.numberOfArithmeticSlices(inp))
