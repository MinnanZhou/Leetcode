class Solution:
    def checkPossibility(self, nums) -> bool:
        used = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if used:
                    return False
                else:
                    used = True
                    if i + 1 < len(nums) and nums[i + 1] < nums[i - 1] and i - 1 >= 0 and nums[i - 2] > nums[i]:
                        return False
        return True


a = Solution()
inp = [1, 2, 3, 1, 2, 4, 5]
print(a.checkPossibility(inp))
