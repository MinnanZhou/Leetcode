class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(x, y, placed):
            if len(placed) == n:
                res[0] += 1
                return True
            if x not in used_r and y not in used_c and x - y not in used_d and x + y not in used_s:
                used_r.add(x)
                used_c.add(y)
                used_d.add(x - y)
                used_s.add(x + y)
                placed.append((x, y))
                for i in range(n):
                    if x == n - 1:
                        if dfs(x + 1, i, placed):
                            used_r.remove(x)
                            used_c.remove(y)
                            used_d.remove(x - y)
                            used_s.remove(x + y)
                            placed.pop()
                            return True
                    else:
                        dfs(x + 1, i, placed)
                used_r.remove(x)
                used_c.remove(y)
                used_d.remove(x - y)
                used_s.remove(x + y)
                placed.pop()
            return False

        res = [0]
        for j in range(n):
            used_c, used_d, used_r, used_s = set(), set(), set(), set()
            dfs(0, j, [])
        return res[0]


a = Solution()
print(a.totalNQueens(9))
