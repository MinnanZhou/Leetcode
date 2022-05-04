class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        ret = [[] for _ in range(numRows)]
        m = 2 * numRows - 2
        for i in range(len(s)):
            pointer = i % m
            ret[min(pointer, m - pointer)].append(s[i])
        res = ''
        for row in ret:
            res += ''.join(row)
        return res


a = Solution()
inp = "P"
print(a.convert(inp, 1))
