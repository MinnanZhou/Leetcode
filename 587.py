class Solution:
    def outerTrees(self, trees):
        def com(p1, p2, p3):
            return (p3[1] - p2[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p2[0])

        trees.sort()
        lower, upper = [], []
        for j in range(len(trees)):
            while len(lower) >= 2 and com(lower[-2], lower[-1], trees[j]) > 0:
                lower.pop()
            while len(upper) >= 2 and com(upper[-2], upper[-1], trees[j]) < 0:
                upper.pop()
            upper.append(tuple(trees[j]))
            lower.append(tuple(trees[j]))
        return list(set(upper + lower))


a = Solution()
inp = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
print(a.outerTrees(inp))
