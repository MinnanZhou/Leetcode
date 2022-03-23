class Solution:
    def increasingTriplet(self, nums) -> bool:
        border = [nums[0], []]
        for i in range(1, len(nums)):
            if nums[i] <= border[0]:
                border[0] = nums[i]
            elif border[1] != [] and nums[i] > border[1]:
                return True
            else:
                border[1] = nums[i]
        return False


a = Solution()
inp=[1,2,4,2,1,3,4,5]
print(a.increasingTriplet(inp))
