class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        s = sum(nums)
        nums.sort(reverse=True)
        target = s // k
        if s % k != 0 or nums[-1] > target: return False
        memory = [0 for _ in range(k)]

        def partition(i):
            if i == len(nums):
                return all(memory[l] == target for l in range(k))
            for j in range(k):
                memory[j] += nums[i]
                if memory[j] <= target and partition(i + 1):
                    return True
                memory[j] -= nums[i]
                if memory[j] == 0:
                    return False
            return False

        return partition(0)


a = Solution()
inp = [4, 3, 2, 3, 5, 2, 1]
print(a.canPartitionKSubsets(inp, 4))
