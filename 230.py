class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        def flatten(tree):
            ret = [tree]
            if tree.left is None and tree.right is None:
                return [tree]
            if tree.left:
                ret = flatten(tree.left)+ret
            if tree.right:
                ret += flatten(tree.right)
            return ret

        return flatten(root)[k-1].val

a = Solution()
inp = [TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), None, None, TreeNode(1)]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]
print(a.kthSmallest(inp[0], 5))
