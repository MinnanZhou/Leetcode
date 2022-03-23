class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        dic_inorder = {}
        for i, val in enumerate(inorder):
            dic_inorder[val] = i

        def recur(left, right):
            if not postorder or right < left:
                return
            tree = TreeNode(postorder.pop())
            root = dic_inorder[tree.val]
            tree.right = recur(root + 1, right)
            tree.left = recur(left, root - 1)
            return tree

        return recur(0, len(postorder) - 1)


a = Solution()
inp = [9, 3, 15, 20, 7]
inp2 = [9, 15, 7, 20, 3]
x = a.buildTree(inp, inp2)
print(x)
