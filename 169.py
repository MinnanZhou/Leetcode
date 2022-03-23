class Solution:
    def majorityElement(self, nums) -> int:
        res = nums[0]
        total = 0
        for i in range(len(nums)):
            if nums[i] == res:
                total += 1
            else:
                if total == 0:
                    res = nums[i]
                    total = 1
                else:
                    total -= 1

        return res
