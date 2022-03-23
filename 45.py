class Solution:
    def jump(self, nums) -> int:
        if len(nums) == 1:
            return 0
        steps = self.callsteps(nums, 0, 0, 0)
        return steps

    def callsteps(self, nums, distance, pos, step):
        result = []
        ran = [i for i in range(pos + 1, pos + nums[pos] + 1)]
        for i in range(len(ran)):
            if i + 1 < len(ran) and ran[i] < len(nums) - 1 and nums[ran[i]] <= nums[ran[i + 1]]:
                continue
            if ran[i] >= len(nums) - 1:
                step += 1
                result.append(step)
            else:
                result.append(self.callsteps(nums, nums[ran[i]] + distance, ran[i], step + 1))
        if not result:
            result.append(len(nums))
        return min(result)

    def steps(self, nums):
        if len(nums)==1:
            return 0
        maxvalue = 0
        i = 0
        ret = 0
        nexti = 0
        while i < len(nums):
            ret += 1
            ran = [j for j in range(i + 1, i + 1 + nums[i])]
            for k in range(len(ran)):
                if ran[k] >= len(nums) - 1:
                    return ret
                if ran[k] + nums[ran[k]] >= maxvalue:
                    maxvalue = ran[k] + nums[ran[k]]
                    nexti = ran[k]
            i = nexti


a = Solution()
inp = [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5]

print(a.steps(inp))
