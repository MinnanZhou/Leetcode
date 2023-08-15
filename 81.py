import bisect
from typing import List


class Solution:
    def search(self, nums, target: int) -> bool:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (j + i) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[i]:
                i += 1
            elif nums[mid] > nums[i]:
                if nums[mid] >= target > nums[i]:
                    j = mid + 1
                else:
                    i = mid - 1
            else:
                if nums[mid] < target <= nums[i]:
                    i = mid - 1
                else:
                    j = mid + 1
        return False

    def search2(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if nums[0] <= nums[n // 2] <= nums[-1]:
            if target < nums[0] or target > nums[-1]: return False
            index = bisect.bisect_left(nums, target)
            return True if nums[index] == target else False
        else:
            left = self.search(nums[:n // 2], target)
            right = self.search(nums[n // 2:], target)
            return left or right


a = Solution()
inp = [1,0,1,1,1]
print(a.search2(inp, 0))
