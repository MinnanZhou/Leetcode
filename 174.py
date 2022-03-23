class Solution:
    def calculateMinimumHP(self, dungeon):
        state = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1, -1):
                if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                    state[i][j] = max(1, 1 - dungeon[i][j])
                elif i == len(dungeon) - 1:
                    state[i][j] = max(1, state[i][j + 1] - dungeon[i][j])
                elif j == len(dungeon[0]) - 1:
                    state[i][j] = max(1, state[i + 1][j] - dungeon[i][j])
                else:
                    state[i][j] = max(1, min(state[i][j + 1], state[i + 1][j]) - dungeon[i][j])
        return state[0][0]


a = Solution()
inp = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
print(a.calculateMinimumHP(inp))
