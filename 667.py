class Solution:
    def constructArray(self, n: int, k: int):
        ret = [1]
        diff = k
        d = 1
        while diff > 0:
            ret.append(ret[-1] + d * diff)
            d = -d
            diff -= 1
        ret += [k + start for start in range(2, n - k + 1)]
        return ret


a = Solution()
print(a.constructArray(20, 15))
