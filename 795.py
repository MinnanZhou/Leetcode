class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        count_total = 0
        count_inside, count_left, count_right = 0, 0, 0
        nums.append(float('inf'))
        for num in nums:
            if num > right:
                count_total += count_left * count_inside + count_right * count_inside + count_left * count_right
                count_total += count_inside * (count_inside + 1) // 2
                count_inside, count_left, count_right = 0, 0, 0
                continue
            if num < left:
                if count_inside:
                    count_right += 1
                else:
                    count_left += 1
            else:
                if not count_right:
                    count_inside += 1
                else:
                    count_total += count_left * count_inside + count_right * count_inside + count_left * count_right
                    count_total += count_inside * (count_inside + 1) // 2
                    count_left += count_inside + count_right
                    count_inside, count_right = 1, 0
        return count_total


a = Solution()
inp = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
print(a.numSubarrayBoundedMax(inp, 32, 69))
