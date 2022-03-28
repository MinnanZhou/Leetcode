class Solution:
    def calcEquation(self, equations, values, queries):
        UnionSet = self.buildTree(equations, values)
        ret = []
        for query in queries:
            find = False
            for _, tree in enumerate(UnionSet):
                if query[0] in tree and query[1] in tree:
                    find = True
                    ret.append(round(tree[query[0]] / tree[query[1]], 5))
                    break
            if not find:
                ret.append(-1.0000)
        return ret

    def buildTree(self, equations, values):
        Union = []
        for i, equation in enumerate(equations):
            value = values[i]
            v1, v2 = None, None
            for index, tree in enumerate(Union):
                if equation[0] in tree:
                    v1 = [tree[equation[0]], index]
                    tree[equation[1]] = tree[equation[0]] / value
                elif equation[1] in tree:
                    v2 = [tree[equation[1]], index]
                    tree[equation[0]] = tree[equation[1]] * value
            if v1 is None and v2 is None:
                Union.append({equation[0]: 1, equation[1]: 1 / value})
            elif v1 is not None and v2 is not None:
                coff = (v1[0] / v2[0]) / value
                for _, k in enumerate(Union[v2[1]]):
                    Union[v1[1]][k] = Union[v2[1]][k] * coff
                del Union[v2[1]]
        return Union


a = Solution()
inp = [["a", "b"], ["b", "c"], ["bc", "cd"]]
inp2 = [1.5, 2.5, 5.0]
inp3 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
print(a.calcEquation(inp, inp2, inp3))
