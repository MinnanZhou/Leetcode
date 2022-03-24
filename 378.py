import bisect
import math


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        stack1 = []
        n = len(matrix)
        left_bound = (1 + n) * n // 2
        if k <= left_bound:
            belong = math.ceil(((8 * k + 1) ** 0.5 - 1) / 2)
            pos = k - (belong - 1) * belong // 2
            for i in range(belong):
                bisect.insort(stack1, matrix[belong - 1 - i][i])
            return stack1[pos - 1]
        else:
            belong = math.ceil(((8 * (n ** 2 + 1 - k) + 1) ** 0.5 - 1) / 2)
            pos = (belong - 1) * belong // 2 - (n ** 2 - k)
            for i in range(-belong, 0):
                bisect.insort(stack1, matrix[i][-belong - 1 - i])
            return stack1[pos - 1]


a = Solution()
inp = [[1,3,5],[6,7,12],[11,14,14]]
print(a.kthSmallest(inp, 3))
