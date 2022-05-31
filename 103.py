from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        res = []

        def getItem(tree, level):
            if tree is None:
                return
            if level > len(res):
                res.append(deque([tree.val]))
            else:
                if level % 2 == 1:
                    res[level - 1].append(tree.val)
                else:
                    res[level - 1].appendleft(tree.val)
            getItem(tree.left, level + 1)
            getItem(tree.right, level + 1)

        getItem(root, 1)

        return res

a = Solution()
inp = [TreeNode(5), TreeNode(3), TreeNode(6), None, None, TreeNode(8), TreeNode(1)]
inp2 = [TreeNode(1)]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]
print(a.zigzagLevelOrder(inp[0]))