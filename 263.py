class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        while abs(n - 2 * int(n / 2)) < 1e-5:
            n = n // 2
        while abs(n - 3 * int(n / 3)) < 1e-5:
            n = n // 3
        while abs(n - 5 * int(n / 5)) < 1e-5:
            n = n // 5
        return abs(n - 1) < 1e-5
