class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                num0 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num0)
            elif i == '-':
                num0 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num0)
            elif i == '*':
                num0 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num0)
            elif i == '/':
                num0 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num0))
            else:
                stack.append(int(i))
        return stack[0]


a = Solution()
inp = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(a.evalRPN(inp))
