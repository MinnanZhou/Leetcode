class Solution:
    def hIndex(self, citations) -> int:
        if max(citations) == 0:
            return 0
        citations = sorted(citations)
        h = len(citations)
        for i in range(h):
            if citations[i] >= h - i:
                return h - i


a = Solution()
inp = [3,3,4]
print(a.hIndex(inp))
