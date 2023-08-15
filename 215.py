import heapq
import random


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        hp = nums[:k]
        heapq.heapify(hp)
        for num in nums[k:]:
            heapq.heappush(hp, num)
            heapq.heappop(hp)
        return hp[0]

    def findKthLargest2(self, nums, k: int) -> int:
        while True:
            pivot = random.randint(0, len(nums) - 1)
            left, middle, right = [], [], []
            for num in nums:
                if num > nums[pivot]:
                    right.append(num)
                elif num < nums[pivot]:
                    left.append(num)
                else:
                    middle.append(num)
            if len(right) < k <= len(right) + len(middle):
                return middle[0]
            else:
                if len(right) >= k:
                    nums = right
                else:
                    nums = left
                    k -= len(right) + len(middle)


a = Solution()
inp = [3, 2, 1, 5, 6, 4]
print(a.findKthLargest2(inp, 6))
