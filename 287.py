class Solution:
    def findDuplicate(self, nums) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


a = Solution()
inp = [1, 3, 4, 2, 2]
print(a.findDuplicate(inp))
