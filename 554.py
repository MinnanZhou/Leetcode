from collections import Counter


class Solution:
    def leastBricks(self, wall) -> int:
        c = Counter()
        for line in wall:
            start = 0
            for brick in line[:-1]:
                start += brick
                c[start] += 1
        return len(wall) - (c.most_common(1)[0][1] if c else 0)


a = Solution()
inp = [[1],[1],[1]]
print(a.leastBricks(inp))
