class Solution:
    def reverse(self, x: int) -> int:
        if -2 ** 31 <= x <= 2 ** 31 - 1:
            if x < 0:
                return -int(str(-x)[::-1])
            else:
                return int(str(x)[::-1])
        return -1
