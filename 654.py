class TreeNode:
    def __init__(self, val=0, left=None, right=None, i=None):
        self.val = val
        self.left = left
        self.right = right
        self.index = i

    def insert(self, val):
        if val[1] > self.index:
            if self.right is None:
                self.right = TreeNode(val=val[0], i=val[1])
            else:
                self.right.insert(val)
        else:
            if self.left is None:
                self.left = TreeNode(val=val[0], i=val[1])
            else:
                self.left.insert(val)


class Solution:
    def constructMaximumBinaryTree(self, nums):
        nums = sorted([[nums[i], i] for i in range(len(nums))], key=lambda x: -x[0])
        b = TreeNode(val=nums[0][0], i=nums[0][1])
        for i in range(1, len(nums)):
            b.insert(nums[i])
        return b


a = Solution()
inp = [3, 2, 1, 6, 0, 5]
print(a.constructMaximumBinaryTree(inp))
