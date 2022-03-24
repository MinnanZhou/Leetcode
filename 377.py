class Solution:
    def combinationSum4(self, nums, target: int):
        nums = sorted(nums)
        prev = {}

        def func(nums, target):
            ret = 0
            for num in nums:
                last = target - num
                if last == 0:
                    ret += 1
                elif last > 0:
                    if last in prev:
                        ret += prev[last]
                    else:
                        ret += func(nums, target - num)
            prev[target] = ret
            return ret

        return func(nums, target)


a = Solution()
inp = [1, 2, 3]
print(a.combinationSum4(inp, 32))
