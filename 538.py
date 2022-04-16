class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root):
        def func(tree, start):
            if not tree:
                return start
            tree.val += func(tree.right, start)
            left = func(tree.left, tree.val)
            return left

        func(root, 0)
        return root


a = Solution()
inp = [TreeNode(4), TreeNode(1), TreeNode(6), TreeNode(0), TreeNode(2), TreeNode(5), TreeNode(7), None, None, None,
       TreeNode(3), None, None, None, TreeNode(8)]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]
print(a.convertBST(inp[0]))
