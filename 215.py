import heapq


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        hp=nums[:k]
        heapq.heapify(hp)
        for num in nums[k:]:
            heapq.heappush(hp,num)
            heapq.heappop(hp)
        return hp[0]

a=Solution()
inp=[3,2,1,5,6,4]
print(a.findKthLargest(inp,2))