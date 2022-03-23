class Solution:
    def combinationSum3(self, k: int, n: int):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ub = sum(nums[-k:])
        lb = sum(nums[0:-k])
        if n > ub or n < lb:
            return []
        results = []
        for i in range(9 - k):
            self.twosum(nums, n, k, [], results, i)

    def twosum(self, nums, target, N, result, results, start):
        if N > 2:
            for i in range(9 - N + 1):
                ret = self.twosum(nums[start + 1:], target - nums[0], N - 1, result, results, start + 1)
                if ret:
                    result += ret
        else:
            left = 0
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return [left, right]


a = Solution()
print(a.combinationSum3(5, 25))
