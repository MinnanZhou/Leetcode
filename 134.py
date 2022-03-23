class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(cost) > sum(gas):
            return -1
        remain = []
        start = 0
        increase = 0
        for i in range(len(gas)):
            remain.append(gas[i] - cost[i])
            if i >= 1:
                if remain[i] - remain[i - 1] > increase:
                    increase = max(increase, remain[i] - remain[i - 1])
                    start = i
        if remain[0] - remain[-1] > increase:
            return 0
        else:
            return start


a = Solution()
inp1 = [6,1,4,3,5]
inp2 = [3,8,2,4,2]
print(a.canCompleteCircuit(inp1, inp2))
