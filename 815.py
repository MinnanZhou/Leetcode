from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        routeDict = defaultdict(set)
        for i, route in enumerate(routes):
            for r in route:
                routeDict[r].add(i)
            routes[i] = set(routes[i])

        path = set()
        station = [source]
        futures = set()
        futureb = set()
        count = 0
        while True:
            while station:
                t = station.pop()
                if t == target:
                    return count
                path.add(t)
                for bus in list(routeDict[t]):
                    futureb.add(bus)
            while futureb:
                b = futureb.pop()
                for sta in routes[b]:
                    if sta not in path: futures.add(sta)
            if not futures: break
            station = list(futures)
            futures.clear()
            count += 1
        return -1


a = Solution()
inp = [[7, 12], [4, 5, 15], [6, 19], [15, 19], [9, 12, 13]]
print(a.numBusesToDestination(inp, 4, 6))
