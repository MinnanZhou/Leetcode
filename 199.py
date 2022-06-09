class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        right = []
        left = []
        if root.right:
            right = self.rightSideView(root.right)
        if root.left:
            left = self.rightSideView(root.left)
        if len(right) >= len(left):
            return [root.val] + right
        else:
            return [root.val] + right + left[len(right):]


a = Solution()
inp = [TreeNode(1), TreeNode(2), TreeNode(3), None, TreeNode(5), None, TreeNode(4), None, None, TreeNode(6)]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]
print(a.rightSideView(inp[0]))
