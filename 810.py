class Solution:
    def xorGame(self, nums) -> bool:
        start = 0
        for num in nums:
            start ^= num
        return True if start == 0 or len(nums) % 2 == 0 else False
