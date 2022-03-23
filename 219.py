class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        count = {}
        interval = float('inf')
        for i in range(len(nums)):
            if nums[i] in count:
                interval = min(interval, i - count[nums[i]])
            count[nums[i]] = i
        return k >= interval


a = Solution()
inp = [1, 2, 3, 3, 2, 3]
print(a.containsNearbyDuplicate(inp, 2))
