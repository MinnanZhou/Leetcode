class Solution:
    def findMinArrowShots(self, points) -> int:
        points = sorted(points, key=lambda x: x[1])
        count, end = 0, float('-inf')
        for point in points:
            if point[0] > end:
                end = point[1]
            else:
                count += 1
        return count


a = Solution()
inp = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(a.findMinArrowShots(inp))
