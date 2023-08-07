from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        numbers = []
        manipulations = []
        i, j = 0, 0
        while i < len(expression):
            if i == len(expression) - 1:
                numbers.append(expression[j:])
            if expression[i] in ['+', '-', '*']:
                manipulations.append(expression[i])
                numbers.append(expression[j:i])
                j = i + 1
            i += 1

        def dc(nums, mans):
            res = []
            if len(nums) == 1:
                return [int(nums[0])]
            for k in range(len(mans)):
                left_nums = nums[:k + 1]
                right_nums = nums[k + 1:]
                left_mans = mans[:k]
                right_mans = mans[k + 1:]
                left_res = dc(left_nums, left_mans)
                right_res = dc(right_nums, right_mans)
                res += cal(left_res, right_res, mans[k])
            return res

        def cal(aa, bb, m):
            if m == '+':
                return [a + b for a in aa for b in bb]
            if m == '-':
                return [a - b for a in aa for b in bb]
            if m == '*':
                return [a * b for a in aa for b in bb]

        return dc(numbers, manipulations)


s = Solution()
print(s.diffWaysToCompute('2*3-4*5'))
