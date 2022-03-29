class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        if len(nums) < 3:
            return 0
        i, count = 1, 0
        while i < len(nums) - 1:
            start = i
            while i < len(nums) - 1 and nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                i += 1
                count += i - start
            i += 1
        return count


a = Solution()
inp = [1, 3, 5, 7, 9, 10, 11, 12, 16, 20, 24, 28, 29]
print(a.numberOfArithmeticSlices(inp))
