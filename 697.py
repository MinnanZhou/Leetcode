from collections import Counter


class Solution:
    def findShortestSubArray(self, nums) -> int:
        c = Counter()
        p = {}
        for i, num in enumerate(nums):
            c[num] += 1
            if num not in p:
                p[num] = [i, i]
            else:
                p[num][0] = min(p[num][0], i)
                p[num][1] = max(p[num][0], i)
        cand = c.most_common()
        j = 0
        ret = len(nums)
        while j < len(cand) and (j == 0 or cand[j][1] == cand[0][1]):
            ret = min(ret, p[cand[j][0]][1] - p[cand[j][0]][0] + 1)
            j += 1
        return ret


a = Solution()
inp = [1]
print(a.findShortestSubArray(inp))
