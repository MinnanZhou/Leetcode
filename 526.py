from functools import cache


class Solution:
    def countArrangement(self, n: int) -> int:
        compare = frozenset([i for i in range(1, n + 1)])

        @cache
        def check(i, array):
            count = 0
            if i == 1:
                return 1
            for num in array:
                if num % i == 0 or i % num == 0:
                    count += check(i - 1, array - {num})
            return count

        return check(n, compare)


a = Solution()
inp = 7
print(a.countArrangement(inp))
