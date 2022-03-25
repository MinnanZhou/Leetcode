class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        def LessorEqual(value):
            count = 0
            index_c, index_r = n - 1, 0
            while index_r < n and index_c >= 0:
                if matrix[index_r][index_c] <= value:
                    count += (index_c + 1)
                    index_r += 1
                else:
                    index_c -= 1
            return count

        lo, hi = matrix[0][0], matrix[-1][-1]
        n = len(matrix)
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            count_LE = LessorEqual(mid)
            if count_LE >= k:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res


a = Solution()
inp = [[10, 40, 70, 110, 150],
       [20, 50, 80, 120, 190],
       [30, 60, 90, 160, 220],
       [100, 130, 140, 170, 240],
       [180, 210, 230, 260, 300]]
print(a.kthSmallest(inp, 5))
