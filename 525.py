class Solution:
    def findMaxLength(self, nums) -> int:
        memory = {0: 0}
        total, last = 0, 0
        for i, num in enumerate(nums):
            last += 1 if num else -1
            if last in memory:
                total = max(total, i - memory[last]+1)
            else:
                memory[last] = i + 1
        return total


a = Solution()
inp = [0]
print(a.findMaxLength(inp))
