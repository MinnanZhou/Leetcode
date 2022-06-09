class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(' ')[::-1]
        i = 0
        while i < len(x):
            if x[i] == '':
                x.pop(i)
            else:
                i += 1
        return ' '.join(x)


a = Solution()
inp = "a good   example"
print(a.reverseWords(inp))
