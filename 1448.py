class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(tree, prevMax):
            if not tree:
                return 0
            if tree.val >= prevMax:
                return count(tree.left, tree.val) + count(tree.right, tree.val) + 1
            else:
                return count(tree.left, prevMax) + count(tree.right, prevMax)

        return count(root, float('-inf'))
