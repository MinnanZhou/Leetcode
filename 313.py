import bisect
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        ugly = primes.copy()
        heapq.heapify(ugly)
        ret = 1
        for _ in range(n - 1):
            ret = heapq.heappop(ugly)
            for prime in primes:
                heapq.heappush(ugly, ret * prime)
                if ret % prime == 0:
                    break
        return ret


a = Solution()
print(a.nthSuperUglyNumber(12, [2, 7, 13, 19]))
