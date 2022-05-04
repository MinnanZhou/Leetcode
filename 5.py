class Solution:
    def longestPalindrome(self, s: str) -> str:
        ins = '$#' + '#'.join(s) + '#%'
        n = len(ins)
        memory = [-1 for _ in range(n)]
        memory[1] = 0
        center = 1
        rightEdge = 1
        maxPos = (0, 0)
        for i in range(1, n - 1):
            rightEdge = max(rightEdge, i + 1)
            if memory[2 * center - i] + i >= memory[center] + center:
                center = i
                while ins[rightEdge] == ins[2 * center - rightEdge]:
                    rightEdge += 1
                memory[i] = rightEdge - i - 1
            else:
                memory[i] = memory[2 * center - i]
            if memory[i] > maxPos[0]: maxPos = (memory[i], i)
        return s[(maxPos[1] - maxPos[0]) // 2:(maxPos[1] + maxPos[0]) // 2]


a = Solution()
inp = "c"
print(a.longestPalindrome(inp))
