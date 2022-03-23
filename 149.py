class Solution:
    def maxPoints(self, points) -> int:
        max_points = 0
        for i in range(len(points)):
            slope_set = {'inf': 1}
            overlap = 0
            x0 = points[i][0]
            y0 = points[i][1]
            for j in range(len(points)):
                x1 = points[j][0]
                y1 = points[j][1]
                if x0 == x1:
                    if y0 == y1:
                        overlap += 1
                    else:
                        slope_set['inf'] += 1
                    continue
                else:
                    slope = round((y0 - y1) / (x0 - x1), 9)
                    if slope in slope_set:
                        slope_set[slope] += 1
                    else:
                        slope_set[slope] = 2
            max_points = max(max_points, max(slope_set.values()))
        return max_points


a = Solution()
inp = [[10000,9999],[0,0],[9999,9998]]
print(a.maxPoints(inp))
