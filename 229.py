class Solution:
    def majorityElement(self, nums):
        res = [0, 1]
        ret = []
        total = [0, 0]
        max_count = [0, 0]
        for num in nums:
            if num == res[0]:
                total[0] += 1
                max_count[0] += 1
            elif num == res[1]:
                total[1] += 1
                max_count[1] += 1
            elif total[0] == 0:
                res[0] = num
                total[0] = 1
                max_count[0] = 1
            elif total[1] == 0:
                res[1] = num
                total[1] = 1
                max_count[1] = 1
            else:
                total[0], total[1] = total[0] - 1, total[1] - 1
        for i in range(2):
            if nums.count(res[i]) >= len(nums) // 3 + 1:
                ret.append(res[i])
        return ret


a = Solution()
inp = [4,2,1,1]
print(a.majorityElement(inp))
