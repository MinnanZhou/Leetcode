from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        memory = set()
        maxLength = 0
        for l in s:
            q.append(l)
            if l in memory:
                while q[0] != l:
                    memory.remove(q.popleft())
                q.popleft()
            else:
                memory.add(l)
            maxLength = max(maxLength, len(q))
        return maxLength


a = Solution()
inp = "pwwkew"
print(a.lengthOfLongestSubstring(inp))
