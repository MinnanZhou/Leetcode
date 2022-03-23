class Solution:
    def singleNumber(self, nums):
        # set1 = set()
        # for i in range(len(nums)):
        #     if nums[i] not in set1:
        #         set1.add(nums[i])
        #     else:
        #         set1.remove(nums[i])
        ret=0
        for num in nums:
            ret= ret^num
        return ret


a = Solution()
inp = [4, 1, 2, 1, 2]
print(a.singleNumber(inp))
