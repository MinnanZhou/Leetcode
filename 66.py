class Solution:
    def plusOne(self, digits):
        digits[-1] += 1
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] == 10:
                if i == (-len(digits)):
                    digits[i] = 0
                    digits.insert(0, 1)
                    break
                digits[i - 1] += 1
                digits[i] = 0
            else:
                break
        return digits


a = Solution()
print(a.plusOne([0]))
