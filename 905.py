class Solution:
    def sortArrayByParity(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
            elif nums[j] % 2 == 1:
                j -= 1
            elif nums[i] % 2 == 0:
                i += 1
        return nums


a = Solution()
inp = [1, 2, 6, 4, 8, 3, 9, 4, 7, 2]
print(a.sortArrayByParity(inp))
