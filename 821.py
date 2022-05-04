class Solution:
    def shortestToChar(self, s: str, c: str):
        ret = [0] * len(s)
        pos = [float('-inf')]
        for i, l in enumerate(s):
            if l == c: pos.append(i)
        pos.append(float('inf'))
        j = 1
        for i, l in enumerate(s):
            ret[i] = min(pos[j] - i, i - pos[j - 1])
            if l == c: j += 1
        return ret


a = Solution()
inp = "loveleetcode"
inp2 = "e"
print(a.shortestToChar(inp, inp2))
