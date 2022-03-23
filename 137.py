class Solution:
    def singleNumber(self, nums):
        count0 = 0
        count1 = 0
        for num in nums:
            count0 = (count0 ^ num) & ~count1
            count1 = (count1 ^ num) & ~count0
        return count0


a = Solution()
inp = [4, 1, 2, 1, 2, 1, 2]
print(a.singleNumber(inp))
