import heapq


class Solution:
    def minCostConnectPoints(self, points) -> int:
        distance = {i: [] for i in range(len(points))}
        mDist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = mDist(points[i], points[j])
                distance[i].append((d, j))
                distance[j].append((d, i))
        visited = {0}
        hp = distance[0]
        heapq.heapify(hp)
        total = 0
        count = 1
        while hp:
            currMin, p = heapq.heappop(hp)
            if p not in visited:
                total += currMin
                visited.add(p)
                for item in distance[p]:
                    heapq.heappush(hp, item)
                count += 1
            if count == len(points): break
        return total


a = Solution()
inp = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(a.minCostConnectPoints(inp))
