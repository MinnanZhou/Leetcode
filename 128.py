class Solution:
    def longestConsecutive(self, nums) -> int:
        dictionary = set(nums)
        res = 0
        for i in dictionary:
            if i - 1 not in dictionary:
                x = i + 1
                while x in dictionary:
                    x += 1
                res = max(res, x - i)
        return res


a = Solution()
inp = [7, 1, 5, 3, 6, 4, 7, 1, 5, 3, 6, 4, 7]
print(a.longestConsecutive(inp))
