class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals = sorted(intervals, key=lambda x: [x[0], -x[1]])
        intervals.append([float('inf'), float('inf')])
        i, j, n, count = 0, 1, len(intervals), 0
        while i < n - 1 and j < n:
            if intervals[i][1] >= intervals[j][1]:
                i += 1
                count += 1
            elif intervals[i][1] <= intervals[j][0]:
                count += j - i - 1
                i = j
            j += 1
        return count


a = Solution()
inp = [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2],
       [30, 47], [-40, -26]]
print(a.eraseOverlapIntervals(inp))
