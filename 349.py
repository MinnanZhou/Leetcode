class Solution:
    def intersection(self, nums1, nums2):
        ret = []
        nums2 = set(nums2)
        for num in nums1:
            if num in nums2:
                ret.append(num)
        return list(set(ret))
