from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        current_path = str(root.val)
        if root.left is not None:
            paths = self.binaryTreePaths(root.left)
            for p in paths:
                res.append(current_path + '->' + p)
        if root.right is not None:
            paths = self.binaryTreePaths(root.right)
            for p in paths:
                res.append(current_path + '->' + p)
        if root.right is None and root.left is None:
            return [current_path]
        return res
