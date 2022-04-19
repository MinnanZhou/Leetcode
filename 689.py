class Solution:
    def maxSumOfThreeSubarrays(self, nums, k: int):
        s1, s2, s3 = sum(nums[:k]), sum(nums[k:2 * k]), sum(nums[2 * k:3 * k])
        r1, r2, r3 = 1, 1+k, 1+2 * k
        l1, l2, l3 = s1, s1 + s2, s1 + s2 + s3
        m1, m2, m3 = [0], [0, k], [0, k, 2 * k]
        while r3 <= len(nums)-k:
            s1 = s1 + nums[r1+k-1] - nums[r1-1]
            s2 = s2 + nums[r2+k-1] - nums[r2-1]
            s3 = s3 + nums[r3+k-1] - nums[r3-1]
            if s1 > l1:
                l1, m1 = s1, [r1]
            if l1 + s2 > l2:
                l2, m2 = l1 + s2, m1 + [r2]
            if l2 + s3 > l3:
                l3, m3 = l2 + s3, m2 + [r3]
            r1 += 1
            r2 += 1
            r3 += 1
        return m3


a = Solution()
inp = [1, 2, 1, 2, 6, 7, 5, 1]
print(a.maxSumOfThreeSubarrays(inp, 2))
