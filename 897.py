class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def rebuild(old):
            if old.left:
                rebuild(old.left)
            nodes.append(TreeNode(old.val))
            if old.right is None:
                return
            else:
                rebuild(old.right)

        rebuild(root)
        for i in range(1, len(nodes)):
            nodes[i - 1].right = nodes[i]
        return nodes[0]


a = Solution()
inp = [TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), None, TreeNode(8), TreeNode(1), None,
       None, None, None, None, TreeNode(7), TreeNode(9)]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]
print(a.increasingBST(inp[0]))
