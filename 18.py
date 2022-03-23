class Solution:
    def func(self, nums, target, curr):
        ret = target + 1
        result = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            for _ in range(len(nums) - 1):
                v = nums[j] + nums[k] + nums[i] - target
                if v == 0:
                    ret = nums[j] + nums[k] + nums[i]
                    result.append([curr, nums[i], nums[j], nums[k]])
                    j += 1
                else:
                    if v > 0:
                        k -= 1
                    else:
                        j += 1
                if j >= k:
                    break
        return int(ret), result

    def fourSum(self, nums, target):
        nums.sort()
        result = []
        ret = []
        for i in range(len(nums) - 3):
            value, position = self.func(nums[i + 1:], target - nums[i], nums[i])
            if value == target - nums[i]:
                result.extend(position)
        for j in result:
            if j not in ret:
                ret.append(j)
        return ret

a=Solution()
inp = [1, 0, -1, 0, -2, 2]
val = 0
print(a.fourSum(inp,val))
