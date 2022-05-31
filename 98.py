class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        def check(left, right, tree):
            if not tree:
                return True
            if tree.val > right or tree.val < left:
                return False
            return check(left, tree.val, tree.left) and check(tree.val, right, tree.right)

        return check(float('-inf'), float('inf'), root)
