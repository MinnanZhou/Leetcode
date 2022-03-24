class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if len(nums) < 2:
            return 1
        count = 1
        state = None
        for index in range(1, len(nums)):
            if nums[index] > nums[index-1] and state != 0:
                count += 1
                state = 0
            elif nums[index] < nums[index-1] and state != 1:
                count += 1
                state = 1
        return count
