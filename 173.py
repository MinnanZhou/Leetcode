from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.data = self.__build(root)
        self.pointer = 0

    def __build(self, tree):
        if not tree: return
        ret = [tree.val]
        if tree.left: ret = self.__build(tree.left) + ret
        if tree.right: ret = ret + self.__build(tree.right)
        return ret

    def next(self) -> int:
        temp = self.data[self.pointer]
        self.pointer += 1
        return temp

    def hasNext(self) -> bool:
        return self.pointer <= len(self.data) - 1


inp = [TreeNode(7), TreeNode(3), TreeNode(15), None, None, TreeNode(9), TreeNode(20)]
for ii, x in enumerate(inp):
    if x and ii * 2 + 1 < len(inp): x.left = inp[ii * 2 + 1]
    if x and (ii + 1) * 2 < len(inp): x.right = inp[(ii + 1) * 2]

a = BSTIterator(inp[0])
