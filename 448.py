class Solution:
    def findDisappearedNumbers(self, nums):
        nums_dict = set(nums)
        n = len(nums)
        ret = []
        for num in range(1, n + 1):
            if num not in nums_dict:
                ret.append(num)
        return ret


a = Solution()
inp = [1,1]
print(a.findDisappearedNumbers(inp))
