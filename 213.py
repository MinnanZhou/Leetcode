class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.func(nums[0:len(nums)-1]),self.func(nums[1:]))
    def func(self, nums):
        if len(nums) == 1:
            return nums[0]
        total = [0 for _ in range(len(nums))]
        total[0], total[1] = nums[0], nums[0] if nums[1] <= nums[0] else nums[1]
        last_robbed = [0 for _ in range(len(nums))]
        last_robbed[0] = 0
        last_robbed[1] = 0 if nums[1] <= nums[0] else 1
        for i in range(2, len(nums)):
            if last_robbed[i - 1] != i - 1:
                total[i] = total[i - 1] + nums[i]
                last_robbed[i] = i
            elif total[i - 1] < total[i - 2] + nums[i]:
                last_robbed[i] = i
                total[i] = total[i - 2] + nums[i]
            else:
                total[i] = total[i - 1]
                last_robbed[i] = last_robbed[i - 1]
        return total[-1]

a = Solution()
inp = [1,2]
print(a.rob(inp))