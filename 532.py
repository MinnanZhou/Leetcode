from collections import Counter


class Solution:
    def findPairs(self, nums, k: int) -> int:
        count = 0
        if k == 0:
            x = Counter(nums).values()
            for item in x:
                if item > 1:
                    count += item * (item - 1) // 2
            return count
        nums = set(nums)
        for num in nums:
            if num - k in nums:
                count += 1
        return count


a = Solution()
inp = [3, 1, 4, 1, 5]
inp2 = 0
print(a.findPairs(inp, inp2))
