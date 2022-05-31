class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:
        return self.isSameTree(root.left, root.right)

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
