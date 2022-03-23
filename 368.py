class Solution:
    def largestDivisibleSubset(self, nums):
        nums = sorted(nums)
        max_d = 1
        res = [[-1, 1] for _ in range(len(nums))]
        for index in range(len(nums)):
            for index2 in range(index):
                if nums[index] % nums[index2] == 0:
                    if res[index2][1] + 1 >= res[index][1]:
                        res[index][0] = index2
                        res[index][1] = res[index2][1] + 1
                        max_d = max(max_d, res[index][1])
        ret = []
        for pos in range(len(nums)):
            if res[pos][1] == max_d:
                while True:
                    ret.append(nums[pos])
                    pos = res[pos][0]
                    if pos == -1:
                        break
                return ret[::-1]


a = Solution()
inp = [1]
print(a.largestDivisibleSubset(inp))
