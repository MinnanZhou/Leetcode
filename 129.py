class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root) -> int:
        values = []

        def getNumber(tree, prefix):
            if tree.left is None and tree.right is None:
                values.append(int(prefix + str(tree.val)))
            elif tree.left is None:
                getNumber(tree.right, prefix + str(tree.val))
            elif tree.right is None:
                getNumber(tree.left, prefix + str(tree.val))
            else:
                getNumber(tree.right, prefix + str(tree.val))
                getNumber(tree.left, prefix + str(tree.val))

        getNumber(root, '')
        return sum(values)
