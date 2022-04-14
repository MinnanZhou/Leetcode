class Solution:
    def findErrorNums(self, nums):
        total = sum(nums)
        n = len(nums)
        nums = set(nums)
        dup = total - sum(list(nums))
        ref = total - n * (n + 1) // 2
        return [dup, dup - ref]


a=Solution()
inp=[1,2,2,4]
print(a.findErrorNums(inp))
