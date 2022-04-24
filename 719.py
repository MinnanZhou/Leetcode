class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        nums.sort()

        def check(val):
            i, j = 0, 0
            count = 0
            while i < len(nums) or j < len(nums):
                while i < len(nums) and nums[i] - nums[j] <= val:
                    i += 1
                count += i - j - 1
                j += 1
            return count >= k

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (right + left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


a = Solution()
inp = [1, 3, 4, 5, 8, 10]
print(a.smallestDistancePair(inp, 6))
