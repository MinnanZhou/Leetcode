class Solution:
    def findDuplicates(self, nums):
        ret = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = -nums[abs(num) - 1]
            else:
                ret.append(abs(num))
        return ret
