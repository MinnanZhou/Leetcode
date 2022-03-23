class Solution:
    def productExceptSelf(self, nums):
        product = 1
        res = []
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                product *= num
        for num in nums:
            if count_zero >= 2:
                return [0 for _ in range(len(nums))]
            elif count_zero == 1:
                if num != 0:
                    res.append(0)
                else:
                    res.append(product)
            else:
                res.append(product // num)
        return res
