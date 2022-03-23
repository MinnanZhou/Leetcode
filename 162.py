class Solution:
    def findPeakElement(self, nums) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left


a = Solution()
inp = [1, 2, 1, 3, 5, 6, 4]
print(a.findPeakElement(inp))
