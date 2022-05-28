class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        current = [(0, 0)]
        new = []
        target = (len(grid) - 1, len(grid[0]) - 1)
        visited = {(0, 0)}
        neighbor = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
        count = 0
        m, n = len(grid), len(grid[0])
        while current:
            count += 1
            while current:
                if current[-1] == target:
                    return count
                x, y = current.pop()
                for dx, dy in neighbor:
                    if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == 0 and \
                            (x + dx, y + dy) not in visited:
                        visited.add((x + dx, y + dy))
                        new.append((x + dx, y + dy))
            current = new.copy()
            new.clear()
        return -1


a = Solution()
inp = [[0, 1], [1, 0]]
print(a.shortestPathBinaryMatrix(inp))
