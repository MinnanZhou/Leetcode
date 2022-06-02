class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum: int):
        def getPath(tree, target, path):
            if tree.left is None and tree.right is None:
                if target == tree.val:
                    res.append(path + [tree.val])
                return
            getPath(tree.left, target - tree.val, path + [tree.val])
            getPath(tree.right, target - tree.val, path + [tree.val])

        res = []
        getPath(root, targetSum, [])
        return res
