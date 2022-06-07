class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        for i in range(len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        count = [i for i in range(-1,len(s))]

        for i in range(len(s)):
            r1, r2 = 0, 0
            while i - r1 >= 0 and i + r1 < len(s) and s[i - r1] == s[i + r1]:
                count[i + r1 + 1] = min(count[i + r1 + 1], count[i - r1] + 1)
                r1 += 1
            while i - r2 >= 0 and i + r2+1 < len(s) and s[i - r2] == s[i + r2+1]:
                count[i + r2 + 2] = min(count[i + r2 + 2], count[i - r2] + 1)
                r2 += 1

        return count[-1]
