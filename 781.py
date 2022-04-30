from collections import Counter


class Solution:
    def numRabbits(self, answers) -> int:
        c = Counter()
        count = 0
        for ans in answers:
            if not c[ans]:
                c[ans] += ans
                count += ans + 1
            else:
                c[ans] -= 1
        return count


a = Solution()
inp = [1]
print(a.numRabbits(inp))
