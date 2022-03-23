import heapq


class Solution:
    def thirdMax(self, nums) -> int:
        nums = list(set(nums))
        hp = nums[:3]
        heapq.heapify(hp)
        for num in nums[3:]:
            heapq.heappush(hp, num)
            heapq.heappop(hp)
        return heapq.heappop(hp) if len(hp) >= 3 else max(hp)


a = Solution()
inp = [1, 2]
print(a.thirdMax(inp))
