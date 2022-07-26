class Solution:
    def countDigitOne(self, n: int) -> int:
        ones = 0
        base = 1
        while base <= n:
            a = n // base
            b = n % base
            ones += ((a + 8) // 10) * base + ((a % 10) == 1) * (b + 1)
            base *= 10
        return ones
