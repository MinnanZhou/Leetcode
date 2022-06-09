class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def calc(num):
            num = str(num)
            res = 0
            for i in num:
                res += int(i) ** 2
            if res == 1:
                return True
            if res in visited:
                return False
            visited.add(res)
            return calc(res)

        return calc(n)


a = Solution()
inp = 345
print(a.isHappy(inp))
