class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for w in s:
            if not stack or w != stack[-1][0]:
                stack.append((w, 1))
            else:
                if stack[-1][1] < k - 1:
                    stack.append((w, stack[-1][1] + 1))
                else:
                    while stack and stack[-1][0] == w:
                        stack.pop()
        return ''.join(stack[i][0] for i in range(len(stack)))


a = Solution()
inp = "deeedbbcccbdaa"
inp2 = 2
print(a.removeDuplicates(inp, inp2))
