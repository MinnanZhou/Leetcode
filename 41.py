class Solution:
    def firstMissingPositive(self, nums) -> int:
        pos = []
        m = 1
        n = 2
        x = [i for i in range(1, len(nums)+1)]
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums)+1:
                continue
            else:
                pos.append(nums[i])
        pos = list(set(pos))
        pos.sort()
        for i in pos:
            if i == m:
                m += 1
                n += 1
            else:
                return n - 1
            # del x[i-1]
        return n - 1


inp = [i for i in range(1,500000)]
del inp[150000]
a = Solution()
print(a.firstMissingPositive(inp))
