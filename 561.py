class Solution:
    def arrayPairSum(self, nums) -> int:
        nums=sorted(nums)
        return sum(nums[::2])