import bisect


class Solution:
    def search(self, nums, target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


a = Solution()
inp = [-1, 0, 3, 5, 9, 12]
print(a.search(inp, 13))
