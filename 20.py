class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}
        stop = {'}', ')', ']'}
        for p in s:
            if stack and stack[-1] in mapping and p == mapping[stack[-1]]:
                stack.pop()
            elif p in stop:
                return False
            else:
                stack.append(p)
        return len(stack) == 0


a = Solution()
inp = '}{'
print(a.isValid(inp))
