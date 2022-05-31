from functools import cache


class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        if len(s1) <= 3 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, len(s1)):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False
