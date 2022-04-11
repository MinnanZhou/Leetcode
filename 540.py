class Solution:
    def singleNonDuplicate(self, nums) -> int:
        i, j = 0, len(nums) - 1
        if i == j: return nums[0]
        while i <= j:
            mid = (i + j) // 2
            if mid > 0 and nums[mid] == nums[mid - 1]:
                if mid % 2 == 1:
                    i = mid + 1
                else:
                    j = mid - 2
            elif mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    i = mid + 2
                else:
                    j = mid - 1
            elif nums[mid] != nums[mid - 1] and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]


a = Solution()
inp = [1,2,2,3,3,4,4]
print(a.singleNonDuplicate(inp))
