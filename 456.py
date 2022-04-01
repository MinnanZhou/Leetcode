class Solution:
    def find132pattern(self, nums) -> bool:
        stack = []
        s3 = float('-inf')
        for num in nums[::-1]:
            if num < s3:
                return True
            else:
                while stack and stack[-1] < num:
                    s3 = stack.pop()
                stack.append(num)
        return False


a = Solution()
inp = [-1, 3, 2, 0]
print(a.find132pattern(inp))
