import bisect


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        left_sorted_array = [nums[0]]
        count = 0
        right_ordered_count = 0
        i = 0
        for i in range(1, len(nums)):
            if nums[i] >= left_sorted_array[-1]:
                left_sorted_array.append(nums[i])
            else:
                break
        max_v = left_sorted_array[-1]
        for j in range(i, len(nums)):
            if nums[j] >= max_v:
                max_v = nums[j]
                right_ordered_count += 1
            else:
                pos = bisect.bisect_right(left_sorted_array, nums[j])
                count += len(left_sorted_array) - pos + right_ordered_count + 1
                left_sorted_array = left_sorted_array[:pos]
                right_ordered_count = 0
        return count


a = Solution()
inp = [2, 6, 4, 8, 10, 9, 15]
print(a.findUnsortedSubarray(inp))
