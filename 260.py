class Solution:
    def singleNumber(self, nums):
        x_xor_y = 0
        for num in nums:
            x_xor_y ^= num
        diff_bit = x_xor_y & (x_xor_y - 1) ^ x_xor_y
        left = 0
        right = 0
        for num in nums:
            temp = num & diff_bit
            if temp == 0:
                left ^= num
            else:
                right ^= num
        return [left, right]


a = Solution()
inp = [1, 2, 1, 3, 2, 5]
print(a.singleNumber(inp))
