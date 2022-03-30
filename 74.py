import bisect


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        matrix_flatten = []
        for row in matrix: matrix_flatten += row
        pos = bisect.bisect_left(matrix_flatten, target)
        return pos != len(matrix_flatten) and matrix_flatten[pos] == target


tar = [1, 3, 5, 7, 10, 11, 16, 20, 21, 22, 23, 30, 34, 61]
inp = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
a = Solution()
for i in tar:
    print(a.searchMatrix(inp, i))
