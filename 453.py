class Solution:
    def minMoves(self, nums) -> int:
        return sum(nums) - len(nums) * min(nums)
