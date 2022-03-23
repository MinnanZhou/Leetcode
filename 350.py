class Solution:
    def intersect(self, nums1, nums2):
        nums1_dict = {}
        ret = []
        for num in nums1:
            if num not in nums1_dict:
                nums1_dict[num] = 1
            else:
                nums1_dict[num] += 1
        for num in nums2:
            if num in nums1_dict and nums1_dict[num] > 0:
                ret.append(num)
                nums1_dict[num] -= 1
        return ret
