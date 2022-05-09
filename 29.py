from math import log10


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        x1, x2 = abs(dividend), abs(divisor)
        if x1==0: return 0
        coff = int(log10(x1))
        while coff >= 0:
            x3 = x2 * 10 ** coff
            while x1 >= x3:
                result += 10 ** coff
                x1 -= x3
            coff -= 1
        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
            return max(-2 ** 31, min(2 ** 31 - 1, result))
        else:
            return max(-2 ** 31, min(2 ** 31 - 1, -result))
