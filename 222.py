class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root) -> int:
        def getLeftHeight(tree):
            if not tree:
                return 0
            return getLeftHeight(tree.left) + 1

        def getRightHeight(tree):
            if not tree:
                return 0
            return getRightHeight(tree.right) + 1

        def getNone(tree, n, r, level):
            if level == 2:
                if n == r:
                    return tree.left
                else:
                    return tree.right
            if n > r:
                return getNone(tree.right, n, r + 2 ** (level - 3), level - 1)
            else:
                return getNone(tree.left, n, r - 2 ** (level - 3), level - 1)

        h = getLeftHeight(root)
        hr = getRightHeight(root)
        if h == hr:
            return 2 ** h - 1
        left, right, mid = 1, 2 ** (h - 1), 0
        while left < right:
            mid = (left + right) // 2
            if getNone(root, mid, 2 ** (h - 2), h):
                left = mid + 1
            else:
                right = mid
        return 2 ** (h - 1) - 2 + left


a = Solution()
inp = [TreeNode(5), TreeNode(3), TreeNode(6),TreeNode(6),TreeNode(6),None, None]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]
print(a.countNodes(inp[0]))
