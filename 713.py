class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        product = 1
        i, j = 0, 0
        nums.append(float('inf'))
        ret = 0
        last = None
        while i < len(nums):
            if product < k:
                product *= nums[i]
                if product >= k:
                    ret += ((i - j) * (i - j + 1) // 2)
                    if last is not None and last >= j: ret -= ((last - j + 1) * (last - j + 2) // 2)
                    last = i - 1
                i += 1
            else:
                product = product // nums[j]
                j += 1
                i = max(i, j)
        return ret


a = Solution()
inp = [3, 2, 1]
print(a.numSubarrayProductLessThanK(inp, 4))
