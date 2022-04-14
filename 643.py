class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        max_value = sum(nums[:k]) / k
        curr = max_value
        for i in range(k, len(nums)):
            curr = curr + (-nums[i - k] + nums[i]) / k
            max_value = max(max_value, curr)
        return max_value


a = Solution()
inp = [0,4,0,3,2]
inp2 = 1
print(a.findMaxAverage(inp, inp2))
