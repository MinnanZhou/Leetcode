class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        s = sum(cardPoints)
        n = len(cardPoints) - k
        local = sum(cardPoints[:n])
        globalMin = local
        for i in range(k):
            local = local - cardPoints[i] + cardPoints[i + n]
            globalMin = min(globalMin, local)
            if globalMin == 0: return s
        return s - globalMin


a = Solution()
inp = [1, 2, 3, 4, 5, 6, 1]
print(a.maxScore(inp, 3))
