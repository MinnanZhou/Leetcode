class Solution:
    def myAtoi(self, s: str) -> int:
        number = ''
        i = 0
        numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        direction = ['+', '-']
        while i < len(s):
            if s[i] == ' ' and len(number) == 0:
                i += 1
                continue
            else:
                if (s[i] in direction and len(number) == 0) or s[i] in numbers:
                    number += s[i]
                    i += 1
                else:
                    break
        number = int(number) if number and number[-1] in numbers else 0
        if number > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if number < -2 ** 31:
            return -2 ** 31
        return number


a = Solution()
inp = "+-12"
print(a.myAtoi(inp))
