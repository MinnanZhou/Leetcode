class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        nums.append(0)
        count, temp = 0, 0
        for num in nums:
            if num:
                temp += 1
            else:
                count = max(temp, count)
                temp = 0
        return count
