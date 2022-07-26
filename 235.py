class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getParents(tree, node):
            if not tree:
                return []
            if tree == node:
                return [tree]
            if node.val > tree.val:
                return [tree] + getParents(tree.right, node)
            return [tree] + getParents(tree.left, node)

        part1 = getParents(root, p)
        part2 = getParents(root, q)
        i = 0
        for i in range(min(len(part1), len(part2))):
            if part1[i] != part2[i]:
                return part2[i - 1]
        return part2[i]
