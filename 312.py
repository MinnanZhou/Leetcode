class Solution:
    def maxCoins(self, nums) -> int:
        nums.insert(0, 1)
        nums.append(1)
        memory = [[0] * len(nums) for _ in range(len(nums))]

        def calculate(i, j):
            if i == j - 1 or memory[i][j]:
                return memory[i][j]
            coins = 0
            for k in range(i + 1, j):
                coins = max(coins, nums[i] * nums[j] * nums[k] + calculate(i, k) + calculate(k, j))
            memory[i][j] = coins
            return coins

        return calculate(0, len(nums) - 1)


a = Solution()
inp = [2,6,4,3,5,7,8,2]
print(a.maxCoins(inp))
