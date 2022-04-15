class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        count = 1
        ret = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                ret = max(ret, count)
                count = 1
        return max(ret, count)


a=Solution()
inp=[1,3,5,4,2,3,4,5]
print(a.findLengthOfLCIS(inp))