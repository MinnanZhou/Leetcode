class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root) -> None:
        if not root: return
        left = self.findMax(root.left)
        right = self.findMin(root.right)
        if left <= root.val <= right:
            self.recoverTree(root.left)
            self.recoverTree(root.right)
        elif left > root.val and root.val <= right:
            self.replace(root.left, left, root.val)
            root.val = left
        elif root.val > right and left <= root.val:
            self.replace(root.right, right, root.val)
            root.val = right
        else:
            self.replace(root.right, right, left)
            self.replace(root.left, left, right)
        pass

    def replace(self, tree, old, new):
        if not tree: return
        if tree.val == old:
            tree.val = new
            return
        else:
            self.replace(tree.left, old, new)
            self.replace(tree.right, old, new)

    def findMax(self, tree: TreeNode):
        if not tree: return float('-inf')
        return max(tree.val, self.findMax(tree.left), self.findMax(tree.right))

    def findMin(self, tree: TreeNode):
        if not tree: return float('inf')
        return min(tree.val, self.findMin(tree.left), self.findMin(tree.right))


a = Solution()
inp = [TreeNode(4),TreeNode(2),TreeNode(6),TreeNode(1),TreeNode(3),TreeNode(7),TreeNode(5)]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]
print(a.recoverTree(inp[0]))
