class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root) -> int:
        globalMax = [0]

        def get(tree):
            if not tree:
                return 0
            leftMax = get(tree.left)
            rightMax = get(tree.right)
            currMax = max(tree.val, tree.val + leftMax, tree.val + rightMax, tree.val + leftMax + rightMax)
            globalMax[0] = max(globalMax[0], currMax)
            return max(tree.val, tree.val + leftMax, tree.val + rightMax, 0)

        get(root)
        return globalMax[0]
