class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) < 2:
            return nums[0]
        if len(nums) < 3:
            return max(nums[0], nums[1], nums[0] * nums[1])
        product = 1
        last_positive = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                product = 1
                continue
            product *= nums[i]
            if product > 0:
                last_positive = max(last_positive, product)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                product = 1
                continue
            product *= nums[i]
            if product > 0:
                last_positive = max(last_positive, product)
        return last_positive


a = Solution()
inp = [0,-1,0,-1]
print(a.maxProduct(inp))
