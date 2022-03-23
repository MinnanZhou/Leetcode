import itertools


class Solution:
    def combine(self, n: int, k: int):
        x = list(itertools.combinations([i for i in range(1, n + 1)], k))
        return x


a = Solution()
print(a.combine(4, 2))
