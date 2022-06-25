class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root) -> int:
        self.total = 0

        def setCamera(tree):
            if not tree:
                return 1
            l, r = setCamera(tree.left), setCamera(tree.right)
            if l == 0 or r == 0:
                self.total += 1
                return 2
            elif l == 2 or r == 2:
                return 1
            else:
                return 0

        if setCamera(root) == 0: self.total += 1
        return self.total
