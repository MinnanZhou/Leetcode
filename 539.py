class Solution:
    def findMinDifference(self, timePoints) -> int:
        timePoints = sorted(timePoints)
        t0 = timePoints[0]
        timePoints.append(str(int(t0.split(':')[0]) + 24) + ':' + t0.split(':')[1])
        res = float('inf')
        for i in range(len(timePoints) - 1):
            t1 = int(timePoints[i].split(':')[0]) * 60 + int(timePoints[i].split(':')[1])
            t2 = int(timePoints[i + 1].split(':')[0]) * 60 + int(timePoints[i + 1].split(':')[1])
            res = min(res, t2 - t1)
            if res == 0:
                return res
        return res


a = Solution()
inp = ["00:00", "23:59", "00:00"]
print(a.findMinDifference(inp))
