class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        pairs = [(s.count('0'), s.count('1')) for s in strs]

        def dp(mm, nn, kk):
            if mm < 0 or nn < 0:
                return -1
            if kk == len(pairs):
                return 0
            x, y = pairs[kk]
            return max(dp(mm, nn, kk + 1), 1 + dp(mm - x, nn - y, kk + 1))

        return dp(m, n, 0)


a = Solution()
print(a.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
