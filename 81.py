class Solution:
    def search(self, nums, target: int) -> bool:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (j + i) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[i]:
                i += 1
            elif nums[mid] > nums[i]:
                if nums[mid] >= target > nums[i]:
                    j = mid + 1
                else:
                    i = mid - 1
            else:
                if nums[mid] < target <= nums[i]:
                    i = mid - 1
                else:
                    j = mid + 1
        return False


a = Solution()
inp = [2, 5, 6, 0, 0, 1, 2]
print(a.search(inp, 0))
