class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        current = [root.val]
        current += self.preorderTraversal(root.left)
        current += self.preorderTraversal(root.right)
        return current
