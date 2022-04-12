class Solution:
    def triangleNumber(self, nums) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            j = len(nums) - 1
            k = j - 1
            while j > i:
                minimum = nums[j] - nums[i]
                while nums[k] > minimum and k > i:
                    k -= 1
                if k == i:
                    count += (j - k - 1) * (j - k) // 2
                    break
                count += (j - k - 1)
                j -= 1
                k = min(k, j - 1)
        return count


a = Solution()
inp = [2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9]
print(a.triangleNumber(inp))
