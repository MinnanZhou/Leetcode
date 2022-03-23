class Solution:
    def steps(self, nums):
        if len(nums) == 1:
            return True
        maxvalue = 0
        i = 0
        ret = 0
        next_i = 0
        while i < len(nums):
            ret += 1
            ran = [j for j in range(i + 1, i + 1 + nums[i])]
            for k in range(len(ran)):
                if ran[k] >= len(nums) - 1:
                    return True
                if ran[k] + nums[ran[k]] >= maxvalue:
                    maxvalue = ran[k] + nums[ran[k]]
                    next_i = ran[k]
            i = next_i
            if nums[i]==0:
                return False


a = Solution()
inp = [8, 1, 1, 1, 1, 1, 1, 1, 1, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5]

print(a.steps(inp))
