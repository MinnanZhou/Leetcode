class Solution:
    def countEven(self, num: int) -> int:
        ten = num // 10
        one = num % 10
        res = ten * 5 - 1
        ten_str=str(ten)
        ten_sum=sum([int(i) for i in ten_str])
        if ten_sum % 2 == 1:
            res += (one + 1) // 2
        else:
            res += one // 2 + 1
        return res


a = Solution()
print(a.countEven(70))
