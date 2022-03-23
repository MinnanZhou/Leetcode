import bisect
from sortedcontainers import SortedList

class Solution:
    def findMaxSum(self, array, bound, m):
        prev = SortedList([0])
        res = float('-inf')
        curr = 0
        for i in range(m):
            curr += array[i]
            idx = prev.bisect_left(curr - bound)
            if idx < len(prev):
                res = max(res, curr - prev[idx])
            prev.add(curr)
        return res

    def maxSumSubmatrix(self, matrix, U: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = float('-inf')
        for i in range(n):
            accu = [0] * m
            for j in range(i, n):
                for k in range(m):
                    accu[k] += matrix[j][k]
                ans = max(ans, self.findMaxSum(accu, U, m))
        return ans


a = Solution()
inp=[]
print(a.maxSumSubmatrix(inp, -5820))
