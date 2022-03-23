class Solution:
    def moveZeroes(self, nums) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1


a = Solution()
inp = [1, 2, 5, 0, 1, 8, 0, 6, 4, 0, 3, 9, 1, 0, 5, 9, 1, 0, 9, 1, 2, 0, 5]
print(a.moveZeroes(inp))
