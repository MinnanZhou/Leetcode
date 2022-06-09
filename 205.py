class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pairs1 = {}
        pairs2 = {}
        i = 0
        while i < len(s):
            if t[i] in pairs1 and pairs1[t[i]] != s[i]:
                return False
            if s[i] in pairs2 and pairs2[s[i]] != t[i]:
                return False
            pairs1[t[i]] = s[i]
            pairs2[s[i]] = t[i]
            i += 1
        return True


a = Solution()
print(a.isIsomorphic('foo', 'bar'))
