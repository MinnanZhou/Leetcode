class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        if 0 < int(s[:2]) <= 26:
            count = self.numDecodings(s[2:]) + self.numDecodings(s[1:])
        else:
            count = self.numDecodings(s[1:])
        return count


a = Solution()
inp = "226"
print(a.numDecodings(inp))
