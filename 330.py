class Solution:
    def minPatches(self, nums, n: int) -> int:
        upper = 0
        i = 0
        patch = 0
        m = len(nums)
        while upper < n:
            if i < m and upper + 1 >= nums[i]:
                upper += nums[i]
                i += 1
            else:
                upper += upper + 1
                patch += 1
        return patch


a = Solution()
inp = [1, 2, 31, 33]

print(a.minPatches(inp, 2147483647))
