class Solution:
    def arrayNesting(self, nums) -> int:
        total_visited = set()
        ret = 0
        for num in nums:
            i = 0
            while num not in total_visited:
                i += 1
                total_visited.add(num)
                num = nums[num]
            ret = max(ret, i)
            if ret > len(nums) // 2: return ret
        return ret


a = Solution()
inp = [5, 4, 0, 3, 1, 6, 2]
print(a.arrayNesting(inp))
