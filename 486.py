from functools import cache


class Solution:
    def PredictTheWinner(self, nums) -> bool:
        @cache
        def dp(i, j):
            return max(nums[i]-dp(i + 1, j), nums[j]-dp(i, j - 1)) if i != j else nums[i]

        return dp(0, len(nums) - 1) >= 0


a = Solution()
inp = [3606449, 6, 5, 9, 452429, 7, 9580316, 9857582, 8514433, 9, 6, 6614512, 753594, 5474165, 4, 2697293, 8, 7, 1]
print(a.PredictTheWinner(inp))
