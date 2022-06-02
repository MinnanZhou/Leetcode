import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root) -> bool:
        def height(tree):
            if tree is None:
                return 0
            return max(height(tree.left), height(tree.right)) + 1

        def check(tree):
            if tree is None:
                return True
            return abs(height(tree.left) - height(tree.right)) <= 1 and check(tree.left) and check(tree.right)

        return check(root)
