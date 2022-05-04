from collections import Counter


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        numsCount = Counter(nums)
        count = 0
        for num in numsCount.keys():
            count += min(numsCount[num], numsCount[k - num])
        return count // 2


a = Solution()
inp = [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2]
print(a.maxOperations(inp, 3))
