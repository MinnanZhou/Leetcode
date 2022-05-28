from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        remain = len(t)
        t = Counter(t)
        i, j = 0, 0
        res = ''
        for i in range(len(s)):
            get = False
            if s[i] in t:
                t[s[i]] -= 1
                if t[s[i]] >= 0:
                    remain -= 1
            while remain == 0:
                get = True
                if s[j] in t:
                    if t[s[j]] == 0:
                        remain += 1
                    t[s[j]] += 1
                j += 1
            if get: res = s[j - 1:i + 1] if len(res) == 0 else min(res, s[j - 1:i + 1], key=lambda x: len(x))
        return res


a = Solution()
inp = "A"
inp2 = "AA"
print(a.minWindow(inp, inp2))
