class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for i in s:
            if s1 and i == '#':
                s1.pop()
            elif i != '#':
                s1.append(i)
        for j in t:
            if s2 and j == '#':
                s2.pop()
            elif j != '#':
                s2.append(j)
        return s1 == s2


a = Solution()
inp1 = '#abc#cdh##jd#'
inp2 = 'abb#ca#j'
print(a.backspaceCompare(inp1, inp2))
