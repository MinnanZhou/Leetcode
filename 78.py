import itertools


class Solution:
    def combine(self, n: int, k: int):
        x = list(itertools.combinations([i for i in range(1, n + 1)], k))
        return x

    def subset(self, nums):
        result = []
        ret = [[]]
        subset = []
        for i in range(len(nums) + 1):
            result += self.combine(len(nums), i)
        for j in result[1:]:
            for k in range(len(j)):
                subset.append(nums[j[k] - 1])
            ret.append(subset)
            subset = []
        return ret


a = Solution()
inp = [2, 4, 6, 8, 10, 12, 14]
print(a.subset(inp))
