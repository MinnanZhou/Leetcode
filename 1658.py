from itertools import accumulate


class Solution:
    def minOperations(self, nums, x: int) -> int:
        cul = [0] + [i for i in accumulate(nums)]
        dic = {i: c for c, i in enumerate(cul)}
        ret = float('inf')
        s = cul[-1] - x
        if s < 0:
            return -1
        for i, val in enumerate(cul):
            if s + val in dic:
                ret = min(ret, len(nums) - dic[s + val] + i)
        return ret if ret != float('inf') else -1


a = Solution()
inp = [1, 1]
print(a.minOperations(inp, 3))
