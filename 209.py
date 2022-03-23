class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        value = 0
        count = len(nums)
        i, j = 0, 0
        for i in range(len(nums)):
            value += nums[i]
            while value - target >= 0:
                count = min(count, i - j + 1)
                value -= nums[j]
                j += 1
        return 0 if value < target and count == len(nums) else count


a = Solution()
inp = 3
inp3 = [1,2,3,2,1]
inp2 = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
print(a.minSubArrayLen(inp, inp3))
