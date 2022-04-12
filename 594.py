from collections import Counter


class Solution:
    def findLHS(self, nums) -> int:
        c = Counter(nums)
        s = set(nums)
        count = 0
        for num in s:
            if num+1 in c:
                count = max(count, c[num] + c[num + 1])
        return count
