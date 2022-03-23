class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        if n != 0:
            i, j = m - 1, n - 1
            for k in range(m + n):
                if nums1[i] >= nums2[j] and i >= 0:
                    nums1[-1 - k] = nums1[i]
                    i -= 1
                else:
                    nums1[-1 - k] = nums2[j]
                    j -= 1
                    if j < 0:
                        break
        return nums1


a = Solution()
print(a.merge([2, 0], 1, [1], 1))
