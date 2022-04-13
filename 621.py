from collections import Counter


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        l = len(tasks)
        tasks = Counter(tasks)
        max_count1 = tasks.most_common(1)[0][1]
        add = list(tasks.values()).count(max_count1)
        return max(l, (max_count1 - 1) * (n + 1) + add)


a = Solution()
inp = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
print(a.leastInterval(inp, 2))
