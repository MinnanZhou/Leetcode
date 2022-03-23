class Solution:
    def summaryRanges(self, nums):
        res = []
        if len(nums) == 0:
            return []
        nums.append(nums[-1] - 1)
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        return res


a = Solution()
inp = [0]
print(a.summaryRanges(inp))
