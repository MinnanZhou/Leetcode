from collections import Counter


class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        ops_s = set([tuple(ops[i]) for i in range(len(ops))])
        min_area = [m, n]
        for s in ops_s:
            min_area[0] = min(min_area[0], s[0])
            min_area[1] = min(min_area[1], s[1])
        return min_area[0] * min_area[1]
