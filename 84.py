class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        heights = [0] + heights + [0]
        n = len(heights)
        res = 0
        for i in range(n):
            # print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[cur])
            stack.append(i)
        return res


a = Solution()
inp = [7, 8, 6, 5, 6, 7, 4]
print(a.largestRectangleArea(inp))
