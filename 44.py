class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        state = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        state[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] != '*':
                break
            state[0][i] = True
        for j in range(1, len(p) + 1):
            for i in range(1, len(s) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    state[i][j] = state[i - 1][j - 1]
                elif p[j - 1] == '*':
                    state[i][j] = state[i - 1][j] or state[i][j - 1]
        return state[-1][-1]


a = Solution()
inp = "aa"
inp2 = "*"
print(a.isMatch(inp, inp2))
