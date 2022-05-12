class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        stack = {0: 0}
        minValue = 0
        countL, countR = 0, 0
        total = 0
        for i, p in enumerate(s):
            if p == '(':
                countL += 1
            else:
                countR += 1
            dp[i + 1] = countL - countR
        for j, diff in enumerate(dp[1:]):
            if diff in stack:
                total = max(total, j - stack[diff]+1)
                stack.pop(diff+1)
            else:
                if diff < minValue:
                    stack.clear()
                    minValue = diff
                stack[diff] = j+1
        return total


a = Solution()
inp = "()(()"
print(a.longestValidParentheses(inp))
