import bisect


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        matrix_flatten = []
        for row in matrix: matrix_flatten += row
        pos = bisect.bisect_left(matrix_flatten, target)
        return pos != len(matrix_flatten) and matrix_flatten[pos] == target

    def searchMatrix2(self, matrix, target: int) -> bool:
        matrix_first_row = [m[0] for m in matrix]
        column_index = bisect.bisect_right(matrix_first_row, target) - 1
        row_index = bisect.bisect_right(matrix[column_index], target) - 1
        return matrix[column_index][row_index] == target


tar = [3]
inp = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
a = Solution()
for i in tar:
    print(a.searchMatrix2(inp, i))
