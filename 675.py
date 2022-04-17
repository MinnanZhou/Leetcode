class Solution:
    def cutOffTree(self, forest) -> int:
        def distance(point1, point2):
            res = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
            p, n = [point1], []
            ob = 0
            visited = set()
            while True:
                if not p:
                    ob += 1
                    p, n = n, p
                x, y = p.pop()
                if (x, y) == point2:
                    return res + ob * 2
                if (x, y) not in visited:
                    visited.add((x, y))
                    for x, y, d in [(x + 1, y, x < point2[0]), (x, y + 1, y < point2[1]), (x - 1, y, x > point2[0]),
                                    (x, y - 1, y > point2[1])]:
                        if forest[x][y]:
                            if d:
                                p.append((x, y))
                            else:
                                n.append((x, y))

        m, n = len(forest), len(forest[0])
        forest.append([0 for _ in range(n)])
        for k in range(m + 1): forest[k].append(0)
        trees = sorted([(forest[i][j], (i, j)) for i in range(m) for j in range(n) if forest[i][j] > 1])
        total = 0
        start = (0, 0)
        queue = [(0, 0)]
        reached = set()
        for i, j in queue:
            if (i, j) not in reached and forest[i][j]:
                reached.add((i, j))
                queue += (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
        if not all((i, j) in reached for _, (i, j) in trees):
            return -1
        for tree in trees:
            total += distance(start, tree[1])
            start = tree[1]
        return total


a = Solution()
inp = [[1, 2, 3], [0, 4, 0], [7, 6, 5]]
print(a.cutOffTree(inp))
