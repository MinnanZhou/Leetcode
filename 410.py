class Solution:
    def splitArray(self, nums, m: int) -> int:
        lower_bound = max(nums)
        upper_bound = sum(nums)
        ret = 0
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            res = self.check(mid, nums, m)
            if res:
                upper_bound = mid - 1
                ret = mid
            else:
                lower_bound = mid + 1
        return ret

    def check(self, limit, nums, m):
        count, total = 1, 0
        for num in nums:
            if total + num > limit:
                count += 1
                total = num
            else:
                total += num
        return count <= m


a = Solution()
inp = [1,2,3,4,5]
print(a.splitArray(inp, 2))
