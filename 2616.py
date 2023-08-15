from typing import List

import numpy as np
from collections import Counter


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            i, k = 1, 0
            mid = (left + right) // 2
            while i < len(nums):
                if nums[i] - nums[i - 1] <= mid:
                    k += 1
                    i += 1
                i += 1
            if k >= p:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
print(s.minimizeMax([3, 4, 2, 3, 2, 1, 2], 3))
