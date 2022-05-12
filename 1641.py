class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n+4)*(n+3)*(n+2)*(n+1)//24


a = Solution()
inp = 50
print(a.countVowelStrings(inp))
