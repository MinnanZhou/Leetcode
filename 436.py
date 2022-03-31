import bisect


class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        index = {intervals[i][0]: i for i in range(n)}
        intervals = sorted(intervals, key=lambda x: x[0])
        start = [intervals[i][0] for i in range(n)]
        ret = [[] for _ in range(n)]
        for interval in intervals:
            pos = bisect.bisect_left(start, interval[1])
            ret[index[interval[0]]] = (-1 if pos >= n else index[intervals[pos][0]])
        return ret


a = Solution()
inp = [[3, 4], [2, 3], [1, 2]]
print(a.findRightInterval(inp))
