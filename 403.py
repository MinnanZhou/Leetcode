from collections import defaultdict


class Solution:
    def canCross(self, stones) -> bool:
        steps = defaultdict(set)
        steps[0].add(1)
        for i in range(len(stones)):
            for _, v in enumerate(steps[stones[i]]):
                if v + stones[i] == stones[-1]:
                    return True
                if v > 1:
                    steps[v + stones[i]].add(v - 1)
                steps[v + stones[i]].add(v)
                steps[v + stones[i]].add(v + 1)
        return False


a = Solution()
inp = [0, 1, 3, 5, 6, 8, 12, 17]
print(a.canCross(inp))
