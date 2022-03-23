from collections import defaultdict, Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        return [i[0] for i in Counter(nums).most_common(k)]


a = Solution()
inp = [1, 1, 1, 2, 2, 3]
print(a.topKFrequent(inp, 2))
