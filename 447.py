from collections import Counter


class Solution:
    def numberOfBoomerangs(self, points) -> int:
        distance = [Counter() for _ in range(len(points))]
        total = 0
        for i in range(len(points)):
            for j in range(len(points)):
                dis = (points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2
                distance[i][dis] += 1
            for value in distance[i].values():
                total += (value * (value - 1))
        return total


a = Solution()
inp = [[0, 0], [1, 0], [2, 0]]
print(a.numberOfBoomerangs(inp))
