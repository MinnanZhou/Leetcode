class Solution:
    def longestCommonPrefix(self, strs) -> str:
        i = 0
        base = min(strs, key=lambda x: len(x))
        while True:
            for s in strs:
                if i >= len(s) or s[i] != base[i]:
                    return s[:i]
            i += 1


a = Solution()
inp = ["flower", "flow", "flight"]
print(a.longestCommonPrefix(inp))
