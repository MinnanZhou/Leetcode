class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def get(tree):
            if not tree:
                return None
            if tree.val == target.val:
                return tree
            else:
                l, r = get(tree.left), get(tree.right)
                if l is not None:
                    return l
                elif r is not None:
                    return r
                else:
                    return None

        return get(cloned)
