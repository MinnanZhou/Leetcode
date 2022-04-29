import bisect


class Solution:
    def isIdealPermutation(self, nums) -> bool:
        for i, num in enumerate(nums):
            if abs(i - num) > 1: return False
        return True


a = Solution()
inp = [2, 0, 1]
print(a.isIdealPermutation(inp))
