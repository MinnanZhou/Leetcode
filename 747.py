class Solution:
    def dominantIndex(self, nums) -> int:
        if len(nums) == 1: return 0
        cache = [float('-inf'), float('-inf'), 0]
        for i, num in enumerate(nums):
            if num > cache[1]:
                cache[0] = cache[1]
                cache[1] = num
                cache[2] = i
            elif num > cache[0]:
                cache[0] = num
        return cache[2] if cache[1] >= 2 * cache[0] else -1


a=Solution()
inp=[1,0]
print(a.dominantIndex(inp))
