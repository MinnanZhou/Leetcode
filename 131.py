class Solution:
    def partition(self, s: str):
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(len(s)):
            if s[0:i + 1] == s[0:i + 1][::-1]:
                temp = [[s[0:i + 1]] + k for k in self.partition(s[i + 1:])]
                res.extend(temp)
        return res


a = Solution()
print(a.partition('bb'))
