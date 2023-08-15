import math
from functools import lru_cache


class Solution:
    def numSquares(self, n: int) -> int:
        if int(math.sqrt(n)) ** 2 == n: return 1
        perfect_squares = [i * i for i in range(int(math.sqrt(n)) + 1)]
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = min([dp[i - j] + 1 for j in perfect_squares[1:int(math.sqrt(i) + 1)]])
        return dp[-1]


s = Solution()
res = s.numSquares(49)
print(res)
