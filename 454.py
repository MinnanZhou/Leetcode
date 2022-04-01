from collections import Counter


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        add = Counter()
        for num1 in nums1:
            for num2 in nums2:
                add[num1 + num2] += 1
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                count += add[-num3 - num4]
        return count
