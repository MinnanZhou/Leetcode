class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []

        res = []
        def getItem(tree, level):
            if tree is None:
                return
            if level > len(res):
                res.append([tree.val])
            else:
                res[level - 1].append(tree.val)
            getItem(tree.left, level + 1)
            getItem(tree.right, level + 1)

        getItem(root, 1)
        return res[::-1]