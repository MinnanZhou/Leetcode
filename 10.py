class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        state = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        state[0][0] = True
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                state[0][j] = state[0][j - 2]
        for j in range(1, len(p) + 1):
            for i in range(1, len(s) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    state[i][j] = state[i - 1][j - 1]
                else:
                    if p[j - 1] == '*':
                        state[i][j] = state[i][j - 1] or state[i][j - 2]
                        if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                            state[i][j] = state[i][j] or state[i - 1][j]
        return state[-1][-1]


a = Solution()
inp = 'abccccccceee'
inp2 = 'a.c*e*e'
print(a.isMatch(inp, inp2))
