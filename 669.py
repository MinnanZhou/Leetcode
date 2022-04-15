class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root, low: int, high: int):
        if not root: return None
        if low < root.val < high:
            root.left = self.trimBST(root.left, low, root.val)
            root.right = self.trimBST(root.right, root.val, high)
            return root
        else:
            if root.val < low: return self.trimBST(root.right, low, high)
            if root.val == low:
                root.left = None
                root.right = self.trimBST(root.right, low, high)
                return root
            if root.val > high: return self.trimBST(root.left, low, high)
            if root.val == high:
                root.right = None
                root.left = self.trimBST(root.left, low, high)
                return root



a = Solution()
inp = [TreeNode(3), TreeNode(-2), TreeNode(6), TreeNode(-3), TreeNode(2), TreeNode(4), TreeNode(7), None, None,
       TreeNode(-1), None, None, TreeNode(5)]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]
print(a.trimBST(inp[0], 5, 6))
