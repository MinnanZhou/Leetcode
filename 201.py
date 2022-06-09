class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            i += 1
            left = left >> 1
            right = right >> 1
        return left << i


a = Solution()
print(a.rangeBitwiseAnd(6, 9))
