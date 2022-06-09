class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        columnNumber -= 1
        while columnNumber >= 0:
            rem = columnNumber % 26
            res += chr(65 + rem)
            columnNumber = columnNumber // 26 - 1
        return res[::-1]


a = Solution()
inp = 1
print(a.convertToTitle(inp))
