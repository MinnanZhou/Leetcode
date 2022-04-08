class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        nums += nums.copy()
        ret = []
        stack = [False]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                stack.append(nums[i + 1])
            elif nums[i] > nums[i + 1]:
                while stack and stack[-1] is not False and stack[-1] <= nums[i]:
                    stack.pop()
            ret.append(stack[-1] if stack[-1] is not False else -1)
        return ret[::-1][:n]


a = Solution()
inp = [1, 8, -1, -100, -1, 222, 1111111, -111111]
print(a.nextGreaterElements(inp))
