class Solution:
    def findSubsequences(self, nums):
        def dp(i):
            if i == len(nums) - 1:
                return [[nums[i]]]
            permu = dp(i + 1)
            for item in permu.copy():
                if nums[i] <= item[-1]:
                    temp = item.copy()
                    temp.append(nums[i])
                    permu.append(temp)
            permu.append([nums[i]])
            return permu

        draft = dp(0)
        ret = set()
        for d in draft:
            if len(d) > 1:
                ret.add(tuple(d[::-1]))
        return list(ret)


a = Solution()
inp = [4,6,7,7]
print(a.findSubsequences(inp))
