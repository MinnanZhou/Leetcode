class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        count, end = 0, float('-inf')
        for i, j in intervals:
            if i >= end:
                end = j
            else:
                count += 1
        return count


a = Solution()
inp = [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2],
       [30, 47], [-40, -26]]
print(a.eraseOverlapIntervals(inp))
