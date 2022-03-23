class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def buildTree(self, preorder, inorder):
    #     root = inorder.index(preorder[0])
    #     tree = TreeNode(preorder[0])
    #     i = [1]
    #     tree.left = self.splittree(inorder[:root], preorder, i)
    #     tree.right = self.splittree(inorder[root + 1:], preorder, i)
    #     return tree
    #
    # def splittree(self, subtree, pretree, i):
    #     if i[0] == len(pretree):
    #         return
    #     if pretree[i[0]] in subtree:
    #         root = subtree.index(pretree[i[0]])
    #         tree = TreeNode(pretree[i[0]])
    #         i[0] += 1
    #         tree.left = self.splittree(subtree[:root], pretree, i)
    #         tree.right = self.splittree(subtree[root + 1:], pretree, i)
    #         return tree
    def buildTree(self, preorder, inorder):
        return self.buildTree2(inorder, preorder, [0])
    def buildTree2(self, inorder, preorder, i):
        if i[0] == len(preorder):
            return
        if preorder[i[0]] in inorder:
            root = inorder.index(preorder[i[0]])
            tree = TreeNode(preorder[i[0]])
            i[0] += 1
            tree.left = self.buildTree2(inorder[:root], preorder, i)
            tree.right = self.buildTree2(inorder[root + 1:], preorder, i)
            return tree


a = Solution()
inp = [1, 2, 4, 8, 9, 14, 15, 5, 3, 6, 10, 11, 7, 12, 13]
inp2 = [8, 4, 14, 9, 15, 2, 5, 1, 10, 6, 11, 3, 12, 7, 13]
x = a.buildTree(inp, inp2)
print(x)
