class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ret = [0] * n
        stack = [(temperatures[-1], n - 1)]
        for i in range(n - 2, -1, -1):
            if temperatures[i] < temperatures[i + 1]:
                ret[i] = 1
            else:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if stack:
                    ret[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return ret


a = Solution()
inp = [7]
print(a.dailyTemperatures(inp))
