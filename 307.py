class Node:
    def __init__(self, start, end):
        self.left_child = None
        self.right_child = None
        self.total = 0
        self.start = start
        self.end = end


class NumArray:

    def __init__(self, nums):
        self.tree = self.build(0, len(nums) - 1, nums)

    def build(self, l, r, nums):
        tree = Node(l, r)
        if l > r:
            return None
        if l == r:
            tree.total = nums[l]
            return tree
        mid = (l + r) // 2
        tree.left_child = self.build(l, mid, nums)
        tree.right_child = self.build(mid + 1, r, nums)
        tree.total = tree.left_child.total + tree.right_child.total
        return tree

    def update(self, index: int, val: int) -> None:
        self.update_tree(index, val, self.tree)

    def update_tree(self, index, val, tree):
        if tree.start == tree.end:
            tree.total = val
        else:
            if index <= (tree.start + tree.end) // 2:
                self.update_tree(index, val, tree.left_child)
                tree.total = tree.left_child.total + tree.right_child.total
            else:
                self.update_tree(index, val, tree.right_child)
                tree.total = tree.left_child.total + tree.right_child.total

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_tree(left, right, self.tree)

    def sum_tree(self, left, right, tree):
        if left == tree.start and right == tree.end:
            return tree.total
        mid = (tree.start + tree.end) // 2
        if left > mid:
            return self.sum_tree(left, right, tree.right_child)
        elif right <= mid:
            return self.sum_tree(left, right, tree.left_child)
        else:
            return self.sum_tree(left, mid, tree.left_child) + self.sum_tree(mid + 1, right, tree.right_child)


a = NumArray([0,9,5,7,3])
print(a.sumRange(4, 4))
print(a.sumRange(2, 4))
print(a.sumRange(3, 3))
a.update(4, 5)
a.update(1, 7)
a.update(0, 8)
print(a.sumRange(1, 2))
a.update(1, 9)
print(a.sumRange(4, 4))
a.update(3, 4)
