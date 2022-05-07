from math import log10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0: return False
        length = int(log10(x)) + 1
        for i in range(length // 2 + 1):
            digitLeft = x // 10 ** (length - i - 1) % 10
            digitRight = x % 10 ** (i + 1) // 10 ** i
            if digitRight != digitLeft:
                return False
        return True


a = Solution()
inp = 12344321
print(a.isPalindrome(inp))
