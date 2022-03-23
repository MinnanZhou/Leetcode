class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]


a = Solution()
inp = [0, 1]
inp2 = [3,4,5,1,2]
print(a.findMin(inp2))
