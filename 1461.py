class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        length = 2 ** k
        start = int('0b' + s[:k], 2)
        values = {start}
        for i in range(k, len(s)):
            start = (start << 1) - int(s[i - k]) * 2 ** k + int(s[i])
            values.add(start)
            if len(values) == length:
                return True
        return False


a = Solution()
inp = "00110"
inp2 = 2
print(a.hasAllCodes(inp, inp2))
