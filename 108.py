class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def func(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                tree = TreeNode(nums[mid])
                tree.left = func(left, mid - 1)
                tree.right = func(mid + 1, right)
                return tree

        return func(0, len(nums) - 1)


a = Solution()
inp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
x = a.sortedArrayToBST(inp)
print(x)
