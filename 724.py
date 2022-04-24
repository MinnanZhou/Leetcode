class Solution:
    def pivotIndex(self, nums) -> int:
        target = sum(nums)
        total = 0
        for i in range(len(nums)):
            if total == ((target - nums[i]) / 2):
                return i
            else:
                total += nums[i]
        return -1


a = Solution()
inp = [-1, -1, -1, -1, -1, -1]
print(a.pivotIndex(inp))
