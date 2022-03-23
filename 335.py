class Solution:
    def isSelfCrossing(self, distance) -> bool:
        for i in range(3, len(distance)):
            if i >= 5 and distance[i - 3] >= distance[i - 1] >= distance[i - 3] - distance[i - 5] and \
                    distance[i - 2] >= distance[i - 4] and distance[i] >= distance[i - 2] - distance[i - 4]:
                return True
            elif (distance[i - 1] < distance[i - 3] and distance[i] >= distance[i - 2]) or \
                    (distance[i - 1] == distance[i - 3] and
                     ((i >= 4 and distance[i] >= distance[i - 2] - distance[i - 4]) or
                     (i < 4 and distance[i] >= distance[i - 2]))):
                return True
            # elif distance[i] > distance[i - 2] and distance[i - 1] > distance[i - 3]:
            #     continue
            # elif distance[i] < distance[i - 2] and distance[i - 1] < distance[i - 3]:
            #     continue
        return False


a = Solution()
inp = [3, 3, 3, 2, 1, 1]
print(a.isSelfCrossing(inp))
