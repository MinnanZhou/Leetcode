class Solution:
    def countAndSay(self, n: int) -> str:
        base = '1#'
        i = 1
        while i < n:
            j = 0
            new = ''
            count = 1
            while j < len(base) - 1:
                if base[j] != base[j + 1]:
                    new += str(count) + base[j]
                    count = 1
                else:
                    count += 1
                j += 1
            base = new + '#'
            i += 1
        return base[:-1]


a = Solution()
print(a.countAndSay(5))
