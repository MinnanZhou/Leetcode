class Solution:
    def optimalDivision(self, nums) -> str:
        if len(nums) == 1: return nums
        if len(nums) == 2: return '/'.join([str(i) for i in nums])
        return str(nums[0]) + '/(' + '/'.join([str(i) for i in nums[1:]]) + ')'
