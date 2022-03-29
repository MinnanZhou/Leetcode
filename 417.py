class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        des = {(0, n - 1): 'AP', (m - 1, 0): 'AP'}
        ret = []

        def check(x, y, visited):
            path = ''
            if x == 0 or y == 0:
                path += 'A'
            if x == m - 1 or y == n - 1:
                path += 'P'
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if ((x + dx, y + dy) not in visited or (x + dx, y + dy) in des) and 0 <= x + dx <= m - 1 and \
                        0 <= y + dy <= n - 1:
                    if heights[x + dx][y + dy] <= heights[x][y]:
                        if (x + dx, y + dy) in des:
                            path += des[(x + dx, y + dy)]
                        else:
                            visited.add((x + dx, y + dy))
                            path += check(x + dx, y + dy, visited)
                            visited.remove((x + dx, y + dy))
                        des[(x, y)] = "".join(set(path))
            des[(x, y)] = "".join(set(path))
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= x + dx <= m - 1 and 0 <= y + dy <= n - 1 and heights[x + dx][y + dy] == heights[x][y]:
                    if (x + dx, y + dy) in des:
                        des[(x + dx, y + dy)] += des[(x, y)]
                    else:
                        des[(x + dx, y + dy)] = des[(x, y)]
                    des[(x + dx, y + dy)] = "".join(set(des[(x + dx, y + dy)]))
            return "".join(set(path))

        for i in range(m):
            for j in range(n):
                if (i, j) in des and (des[(i, j)] == 'AP' or des[(i, j)] == 'PA'):
                    ret.append([i, j])
                else:
                    res = check(i, j, {(i, j)})
                    if res == 'AP' or res == 'PA':
                        ret.append([i, j])
        return ret


a = Solution()
inp = []
print(a.pacificAtlantic(inp))
