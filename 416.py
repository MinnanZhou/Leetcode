from functools import cache


class Solution:
    def canPartition(self, nums) -> bool:
        @cache
        def cal(x, i=0):
            if x == 0:
                return True
            elif x < 0 or i >= len(nums):
                return False
            else:
                return cal(x - nums[i], i + 1) or cal(x, i + 1)

        total = sum(nums)
        return total % 2 == 0 and cal(total // 2)


a = Solution()
inp = [1,2,5]
print(a.canPartition(inp))
