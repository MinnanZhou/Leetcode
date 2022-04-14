class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val: int):
        def check(value, tree):
            if tree is None:
                return None
            if value == tree.val:
                return tree
            elif value > tree.val:
                return check(value, tree.right)
            else:
                return check(value, tree.left)

        return check(val, root)


a = Solution()
inp = [4, 2, 7, 1, 3]


def build(i, tree):
    if (i + 1) * 2 <= len(inp) - 1:
        right_tree = TreeNode(val=inp[(i + 1) * 2])
        tree.right = build((i + 1) * 2, right_tree)
    if (i + 1) * 2 - 1 <= len(inp) - 1:
        left_tree = TreeNode(val=inp[(i + 1) * 2 - 1])
        tree.left = build((i + 1) * 2 - 1, left_tree)
    return tree


Tree = TreeNode(val=inp[0])
print(a.searchBST(build(0, Tree), 2))
