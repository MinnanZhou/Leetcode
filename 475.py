import bisect


class Solution:
    def findRadius(self, houses, heaters) -> int:
        heaters.sort()
        max_radius = float('-inf')
        for house in houses:
            pos = bisect.bisect_left(heaters, house)
            if pos == 0 or pos == len(heaters):
                curr_radius = abs(house - heaters[pos])
            else:
                curr_radius = min(abs(house - heaters[pos]), abs(house - heaters[pos - 1]))
            max_radius = max(max_radius, curr_radius)
        return max_radius


a = Solution()
inp = [1, 2, 4, 5]
inp2 = [0, 2, 7]
print(a.findRadius(inp, inp2))
