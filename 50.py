class Solution:
    def myPow(self, x: float, n: int) -> float:
        def multiply(t):
            if t == 0:
                return 1
            if t == 1:
                return x
            val = multiply(t // 2)
            if abs(val) > 10000: val = -10000 if val < 0 else 10000
            return val ** 2 if t % 2 == 0 else val ** 2 * x

        value = multiply(abs(n))
        return value if n >= 0 else 1 / value


a = Solution()
print(a.myPow(2, -1))
