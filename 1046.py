import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones.append(0)
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, -abs(s1 - s2))
        return -stones[0]


a = Solution()
inp = [2, 7, 4, 1, 8, 1]
print(a.lastStoneWeight(inp))
