from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(list(s))
        count = sorted(c.values(), reverse=True)
        total = 0
        for i, v in enumerate(count[:-1]):
            if count[i] <= count[i + 1]:
                if count[i] > 0:
                    total += count[i + 1] - count[i] + 1
                    count[i + 1] = count[i] - 1
                else:
                    total += count[i + 1]
                    count[i + 1] = 0
        return total


a = Solution()
inp = "aab"
print(a.minDeletions(inp))
