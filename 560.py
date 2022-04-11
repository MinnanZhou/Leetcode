from collections import Counter


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        part_sum = [nums[0]]
        for i in range(1, len(nums)):
            part_sum.append(part_sum[-1] + nums[i])
        res = 0
        part_sum_c = Counter()
        for i in range(len(part_sum)):
            if part_sum[i] == k: res += 1
            res += part_sum_c[part_sum[i] - k]
            part_sum_c[part_sum[i]] += 1
        return res


a = Solution()
inp = [-1,-1,1]
print(a.subarraySum(inp, 0))
