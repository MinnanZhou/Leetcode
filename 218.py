import heapq


class Solution:
    def getSkyline(self, buildings):
        res = [[0, 0]]
        hp = [[0, float('inf')]]
        heapq.heapify(hp)
        events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for l, r, h in buildings}))
        for l, n_h, r in events:
            while l >= hp[0][1]:
                heapq.heappop(hp)
            if n_h != 0:
                heapq.heappush(hp, [n_h, r])
            if hp[0][0] != -res[-1][1]:
                res.append([l, -hp[0][0]])
        return res[1:]


a = Solution()
inp = [[2, 6, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(a.getSkyline(inp))
