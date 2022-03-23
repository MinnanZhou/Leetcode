import bisect


class Solution:
    def countSmaller(self, nums):
        ret = [0]
        count = [nums[-1]]
        nums.reverse()
        for i in range(1, len(nums)):
            pos = bisect.bisect_left(count, nums[i])
            count.insert(pos, nums[i])
            if nums[i] == nums[i - 1]:
                ret.append(ret[-1])
            else:
                ret.append(pos)
        ret.reverse()
        return ret


a = Solution()
inp = [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97, 3,
       76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]
print(a.countSmaller(inp))
