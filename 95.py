class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        def build(start, end):
            if start > end:
                return [None]
            res = []
            for v in range(start, end + 1):
                leftCandidates = build(start, v - 1)
                rightCandidates = build(v + 1, end)
                for l in leftCandidates:
                    for r in rightCandidates:
                        root = TreeNode(v)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        x = build(1, n)
        return x


a = Solution()
print(a.generateTrees(3))
