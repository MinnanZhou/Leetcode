from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [True, False, nums[0] == nums[1]]
        for i in range(2, len(nums)):
            if not any(dp):
                return False
            last_attempt = False
            if nums[i] == nums[i - 1] and dp[1]:
                last_attempt = True
            elif nums[i] == nums[i - 1] == nums[i - 2] and dp[0]:
                last_attempt = True
            elif nums[i] - nums[i - 1] == 1 and nums[i - 1] - nums[i - 2] == 1 and dp[0]:
                last_attempt = True
            dp[0], dp[1], dp[2] = dp[1], dp[2], last_attempt
        return dp[-1]
