class Solution:
    def maximalRectangle(self, matrix) -> int:
        cmat = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    cmat[i][j] += 1
                    k = i
                    while k != 0:
                        if int(matrix[k - 1][j]) != 0:
                            cmat[k - 1][j] += 1
                            k -= 1
                        else:
                            break
        res = 0
        for i in range(len(cmat)):
            res = max(res, self.largestRectangleArea(cmat[i]))
        return res

    def largestRectangleArea(self, height) -> int:
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans


a = Solution()
inp = [["1", "0", "1", "1", "1"], ["0", "1", "0", "1", "0"], ["1", "1", "0", "1", "1"], ["1", "1", "0", "1", "1"], ["0", "1", "1", "1", "1"]]
print(a.maximalRectangle(inp))
