class Solution:
    def maximumGap(self, nums) -> int:
        hi = max(nums)
        lo = min(nums)
        n = len(nums)
        if n <= 2 or hi == lo:
            return hi - lo
        bucket = [[[], []] for _ in range(n - 1)]
        gap = 0
        width = max(1, (hi - lo) // (n - 1))
        for i in range(n):
            group = int((nums[i] - lo) / width)
            if group >= n - 1:
                group = n - 2
            if not bucket[group][0]:
                bucket[group][0] = bucket[group][1] = nums[i]
            else:
                if nums[i] > bucket[group][1]:
                    bucket[group][1] = nums[i]
                elif nums[i] < bucket[group][0]:
                    bucket[group][0] = nums[i]
        accu = 0
        for index in range(n - 2):
            if not bucket[index + 1][0]:
                accu += 1
                continue
            else:
                gap = max(gap, bucket[index + 1][0] - bucket[index - accu][1])
                accu = 0
        return gap


a = Solution()
inp = [1, 1, 1, 1, 1, 2,2,2,2,2]
print(a.maximumGap(inp))
