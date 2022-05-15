from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        remain = [str(i) for i in range(1, n + 1)]

        def get(n, k):
            if n <= 2:
                return ''.join(remain) if k == 1 else ''.join(remain[::-1])
            fac = factorial(n - 1)
            current = remain.pop((k - 1) // fac)
            ret = current + get(n - 1, k % fac)
            return ret

        return get(n, k)


a = Solution()
print(a.getPermutation(6, 118))
