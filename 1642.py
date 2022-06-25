import heapq


class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        bricksNeeded = [0 for _ in range(len(heights) - 1)]
        for i in range(len(heights) - 1):
            bricksNeeded[i] = max(0, heights[i + 1] - heights[i])
        i, hp = 0, []
        while i < len(heights) - 1:
            if len(hp) < ladders:
                heapq.heappush(hp, bricksNeeded[i])
            else:
                if bricksNeeded[i] <= hp[0]:
                    bricks -= bricksNeeded[i]
                else:
                    bricks -= heapq.heappushpop(hp, bricksNeeded[i])
            if bricks < 0:
                break
            i += 1
        return i


a = Solution()
inp = [4, 2, 7, 6, 9, 14, 12]
inp2 = 5
inp3 = 1
print(a.furthestBuilding(inp, inp2, inp3))
