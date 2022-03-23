class Solution:
    def lengthOfLIS(self, nums) -> int:
        sub = [nums[0]]
        for i in nums[1:]:
            if i > sub[-1]:
                sub.append(i)
            elif i != sub[-1]:
                ins = self.search(sub, i)
                sub[ins] = min(i, sub[ins])
        return len(sub)

    def search(self, nums, target):
        i = 0
        k = len(nums) - 1
        j = (k - i) // 2
        if len(nums) == 0:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        while True:
            if nums[j] == target:
                return j
            elif nums[j] > target:
                k = j
                j = round((k + i) / 2 - 0.01)
                m = 1
            else:
                i = j
                j = round((k + i) / 2 + 0.01)
                m = 0
            if k - i <= 1:
                j = j + m
                break
        return j
