class Solution:
    def findRepeatedDnaSequences(self, s: str):
        visited = {s[:10]}
        ret = set()
        for i in range(1, len(s) - 9):
            if s[i:i + 10] in visited:
                ret.add(s[i:i + 10])
            else:
                visited.add(s[i:i + 10])
        return ret

a=Solution()
inp='AAAAAAAAAAA'
print(a.findRepeatedDnaSequences(inp))