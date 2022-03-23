class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, min(h, w) ** 2)
                stack.append(i)
        return ans

    def dp(self, matrix):
        state_grid = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        # for line in state_grid:
        #     line.insert(0, 0)
        # state_grid.insert(0, [0 for _ in range(len(state_grid[0]))])
        # dial = min(len(matrix), len(matrix[0]))
        # state = [[0 for _ in range(dial - 1)], [0 for _ in range(dial)]]
        edge = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    state_grid[i + 1][j + 1] = min(state_grid[i + 1][j], state_grid[i][j + 1], state_grid[i][j]) + 1
                    edge = max(edge, state_grid[i + 1][j + 1])
        return edge ** 2


a = Solution()
inp = [["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"],
       ["0", "0", "1", "1", "1"]]
print(a.dp(inp))
