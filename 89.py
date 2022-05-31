class Solution:
    def grayCode(self, n: int):
        ret = [0]
        for i in range(n):
            ret += [x + 2 ** i for x in ret[::-1]]
        return ret
