class Solution:
    def missingNumber(self, nums):
        nums = dict.fromkeys(nums,1)
        candidate = []
        for num in nums:
            if num + 1 not in nums:
                candidate.append(num + 1)
        return min(candidate)


a = Solution()
inp = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(a.missingNumber(inp))
