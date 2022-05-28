class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        start = 0
        end = x
        mid = x
        while abs(mid * mid - x) > 0.01:
            mid = (end + start) / 2
            if mid * mid == x:
                return int(mid)
            if mid * mid < x:
                start = mid
            else:
                end = mid
        return int(mid)


a = Solution()
print(a.mySqrt(9))
