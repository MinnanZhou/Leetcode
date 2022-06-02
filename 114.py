class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root) -> None:
        def traverse(tree):
            if tree is None:
                return
            nodes.append(tree)
            traverse(tree.left)
            traverse(tree.right)

        nodes = []
        traverse(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
