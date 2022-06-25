class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        i, j = 0, 0
        used = set()
        localSum = 0
        maxSum = 0
        while j < len(nums):
            if nums[j] not in used:
                used.add(nums[j])
                localSum += nums[j]
                maxSum = max(maxSum, localSum)
                j += 1
            else:
                while nums[i] != nums[j]:
                    used.remove(nums[i])
                    localSum -= nums[i]
                    i += 1
                used.remove(nums[i])
                localSum -= nums[i]
                i += 1
        return maxSum
