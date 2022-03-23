class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        visited = set()
        for i in range(len(s)):
            last.update([(s[i], i)])
        stack = ['!']
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while s[i] < stack[-1] and last[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(s[i])
            visited.update(s[i])
        return "".join(stack)[1:]


a = Solution()
inp = "bdabzd"
print(a.removeDuplicateLetters(inp))
