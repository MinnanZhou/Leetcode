class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root) -> int:
        def find(tree, level):
            if not tree:
                return [None, -1]
            left, leftLevel = find(tree.left, level + 1)
            right, rightLevel = find(tree.right, level + 1)
            if left is None and right is None:
                return [tree.val, level]
            elif left is not None and right is not None:
                if leftLevel == rightLevel:
                    return [left + right, leftLevel]
                else:
                    return [left, leftLevel] if leftLevel > rightLevel else [right, rightLevel]
            else:
                return [left, leftLevel] if left is not None else [right, rightLevel]

        return find(root, 0)[0]
