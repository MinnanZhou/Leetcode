import heapq
import numpy as np


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1: return 1
        t2, t3, t5 = 0, 0, 0
        k = [0] * n
        k[0] = 1
        for i in range(1, n):
            k[i] = min([k[t2] * 2, k[t3] * 3, k[t5] * 5])
            t2 += k[i] == k[t2] * 2
            t3 += k[i] == k[t3] * 3
            t5 += k[i] == k[t5] * 5
        return k[-1]


s = Solution()
res = s.nthUglyNumber(1690)
print(res)
