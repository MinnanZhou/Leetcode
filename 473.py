from functools import cache


class Solution:
    def makesquare(self, matchsticks) -> bool:
        matchsticks = sorted(matchsticks, reverse=True)
        basket, rem = divmod(sum(matchsticks), 4)
        if rem or matchsticks[0] > basket: return False

        edge = [0, 0, 0, 0]

        def dfs(matches, square):
            if len(matches) == 0:
                return square[0] == square[1] == square[2] == square[3]
            for i in range(4):
                if any([square[i] == square[j] for j in range(i)]): continue
                square[i] += matches[0]
                if square[i] <= basket and dfs(matches[1:], square):
                    return True
                square[i] -= matches[0]
            return False

        return dfs(matchsticks, edge)


a = Solution()
inp = [5969561, 8742425, 2513572, 3352059, 9084275, 2194427, 1017540, 2324577, 6810719, 8936380, 7868365, 2755770,
       9954463, 9912280, 4713511]
print(a.makesquare(inp))
