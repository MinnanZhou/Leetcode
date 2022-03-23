class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        col = [i[0] for i in matrix]
        colpos = self.findcolpos(col, target, 0, len(col) - 1)
        return self.binary(matrix[colpos-1], target, 0, len(matrix[colpos-1]) - 1)

    def findcolpos(self, nums, target, left, right):
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid+1
        return left

    def binary(self, nums, target, left, right):
        if nums[(right + left) // 2] == target:
            return True
        elif right - left < 1:
            return False
        elif nums[(right + left) // 2] > target:
            return self.binary(nums, target, left, (left + right) // 2 - 1)
        else:
            return self.binary(nums, target, (left + right) // 2 + 1, right)


tar = [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
inp = [[1], [3], [5], [7]]
a = Solution()
for i in tar:
    print(a.searchMatrix(inp, i))
