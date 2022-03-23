class Node:
    def __init__(self, start, end):
        self.left_child = None
        self.right_child = None
        self.start = start
        self.end = end
        self.cnt = 0


class NumArray:

    def __init__(self, nums):
        self.tree = self._build(0, len(nums) - 1, nums)


    def _build(self, l, r, nums):
        tree = Node(nums[l], nums[r])
        if l >= r:
            return tree
        mid = (l + r) // 2
        tree.left_child = self._build(l, mid, nums)
        tree.right_child = self._build(mid + 1, r, nums)
        return tree

    def update(self, tree, val):
        if not tree:
            return
        if tree.start <= val <= tree.end:
            tree.cnt += 1
            self.update(tree.left_child, val)
            self.update(tree.right_child, val)

    def query(self, tree, lower, upper):
        if lower <= tree.start and tree.end <= upper:
            return tree.cnt
        if upper < tree.start or tree.end < lower:
            return 0
        return self.query(tree.left_child, lower, upper) + self.query(tree.right_child, lower, upper)




class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1] + n)

        cumsum_ordered = sorted(list(set(cumsum)))  # need sorted
        root = NumArray(cumsum_ordered)

        res = 0
        for csum in cumsum:
            res += root.query(root.tree, csum - upper, csum - lower)
            root.update(root.tree, csum)
        return res



a = Solution()
inp = [0]
print(a.countRangeSum(inp, 0, 0))
