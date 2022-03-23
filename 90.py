import itertools


class Solution:
    def subsetsWithDup(self, nums):
        ret = []
        res = [[]]
        nums = sorted(nums)
        for i in range(len(nums) + 1):
            ret.extend(list(itertools.combinations(nums, i)))
        for i in range(1, len(ret)):
            if list(ret[i]) not in res:
                res.append(list(ret[i]))
        return res

    def func(self, nums):
        prev = {()}
        for num in sorted(nums):
            nxt = set()
            for p in prev:
                to_add = (*p, num)
                if to_add not in prev:
                    nxt.add(to_add)
            prev = prev.union(nxt)

        return sorted([list(p) for p in prev])


a = Solution()
inp = [2, 1, 2, 1, 3]
print(a.func(inp))
