import bisect
from typing import List


def func(nums, target):
    if len(nums) < 3:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        else:
            return -1
    if nums[0] < nums[-1]:
        j = 0
        l = 0
        n = len(nums) - 1
    else:
        i = 0
        k = len(nums) - 1
        j = (i + k) // 2
        while True:
            if nums[j] > nums[k]:
                i = j
                j = round((i + k) / 2 + 0.01)
            elif nums[j] < nums[k]:
                k = j
                j = round((i + k) / 2)
            else:
                break
        l = j - len(nums)
        n = j - 1
    m = round((l + n) / 2)
    index = 2
    while True:
        if (2 ** (index - 2)) > len(nums):
            break
        else:
            step = (len(nums) / (2 ** index))
            if int(step) == 0:
                if step > 0:
                    step = 1
            else:
                step = round(step)
        if nums[m] == target:
            return m % len(nums)
        elif nums[m] > target:
            m = m - step
        else:
            m = m + step
        index += 1
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums[0] <= nums[-1]:
            if target < nums[0] or target > nums[-1]: return -1
            index = bisect.bisect_left(nums, target)
            return index if nums[index] == target else -1
        else:
            left = self.search(nums[:n // 2], target)
            if left != -1: return left
            right = self.search(nums[n // 2:], target)
            if right != -1: return right + n // 2
            return -1


s = Solution()
inp = [4, 5, 6, 7, 0, 1, 2]
goal = 0
print(s.search(inp, goal))
