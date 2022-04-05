import bisect


class Solution:
    def reversePairs(self, nums) -> int:
        st = []
        count = 0
        for num in nums:
            count += len(st) - bisect.bisect_right(st, num * 2)
            bisect.insort_right(st, num)
        return count


a = Solution()
inp = [5, 2, 3, 2, 3, 1]
print(a.reversePairs(inp))
