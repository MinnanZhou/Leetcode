class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if len(nums) == 1 or k == 0:
            return False
        k = min(len(nums) - 1, k)
        window = nums[0:k + 1]
        window = sorted(window)
        min_value = float('inf')
        for i in range(1, k + 1):
            min_value = min(min_value, window[i] - window[i - 1])
        for i in range(0, len(nums) - k - 1):
            window.remove(nums[i])
            ins = self.findinsert(window, nums[k + 1 + i])
            window.insert(ins, nums[k + 1 + i])
            if ins == 0:
                min_value = min(min_value, window[1] - window[0])
            elif ins == k:
                min_value = min(min_value, window[k] - window[k - 1])
            else:
                min_value = min(min_value, window[ins] - window[ins - 1], window[ins + 1] - window[ins])
        return True if min_value <= t else False

    def findinsert(self, nums, target):
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


a = Solution()
inp = [1, 2]
inp2 = 0
inp3 = 1
print(a.containsNearbyAlmostDuplicate(inp, inp2, inp3))
