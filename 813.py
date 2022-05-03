class Solution:
    def largestSumOfAverages(self, nums, k: int) -> float:
        memory = {}
        m = len(nums)

        def dp(n, x):
            if (n, x) in memory:
                return memory[(n, x)]
            if n <= 0 or x <= 0 or n < x: return 0
            if x == 1:
                memory[(n, x)] = sum(nums[:n]) / n
                return memory[(n, x)]
            maxValue = 0
            for i in range(n, -1, -1):
                maxValue = max(maxValue, dp(i - 1, x - 1) + sum(nums[i - 1:n]) / (n - i + 1))
            memory[(n, x)] = maxValue
            return maxValue

        return dp(m, k)


a = Solution()
inp = [1, 2, 3, 4, 5, 6, 7]
inp2 = 4
print(a.largestSumOfAverages(inp, inp2))
