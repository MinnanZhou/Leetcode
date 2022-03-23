import bisect


class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        ret = []
        for _, height in envelopes:
            pos = bisect.bisect_left(ret, height)
            if pos == len(ret):
                ret.append(height)
            else:
                ret[pos] = height
        return len(ret)


a = Solution()
inp = [[30, 50], [12, 2], [3, 4], [12, 15]]
print(a.maxEnvelopes(inp))
