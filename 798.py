class Solution:
    def bestRotation(self, nums) -> int:
        N = len(nums)
        change = [1] * N
        for i in range(N):
            change[(i - nums[i] + 1) % N] -= 1
        v, k = change[0], 0
        for i in range(1, N):
            change[i] += change[i - 1]
            if change[i] > v:
                v = change[i]
                k = i
        return k


a = Solution()
inp = [3, 0, 2, 1, 5, 4]
print(a.bestRotation(inp))
