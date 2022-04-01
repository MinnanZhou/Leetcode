class Solution:
    def findContentChildren(self, g, s) -> int:
        g, s = sorted(g, reverse=True), sorted(s, reverse=True)
        i, j = 0, 0
        count = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                i += 1
                count += 1
            j += 1
        return count
