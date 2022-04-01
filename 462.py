class Solution:
    def minMoves2(self, nums) -> int:
        nums = sorted(nums)
        n = len(nums)
        return sum([abs(nums[n // 2] - nums[i]) for i in range(n)])
