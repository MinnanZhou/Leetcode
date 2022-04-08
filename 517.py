class Solution:
    def findMinMoves(self, machines) -> int:
        if sum(machines) % len(machines) != 0: return -1
        target = sum(machines) // len(machines)
        machines.append(target)
        ls = machines[0]
        count = 0
        last_diff = 0
        for i, m in enumerate(machines[1:]):
            diff = ls - target * (i + 1)
            if last_diff >= 0 and diff >= 0:
                count = max(count, abs(last_diff + diff))
            else:
                count = max(count, max(abs(last_diff), abs(diff)))
            last_diff = -diff
            ls += m
        return count


a = Solution()
inp = [9, 1, 8, 8, 9]
print(a.findMinMoves(inp))
