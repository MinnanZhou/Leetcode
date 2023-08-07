from functools import lru_cache


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @lru_cache(None)
        def dp(unplayed, played, cooldown, target):
            if unplayed > target:
                return 0
            if cooldown == 0:
                cooldown = 1
                played += 1
            if target == 0:
                return 1
            res = 0
            if played > 0:
                res += dp(unplayed, played - 1, cooldown - 1, target - 1) * played
            if unplayed > 0:
                res += dp(unplayed - 1, played, cooldown - 1, target - 1) * unplayed
            return res

        return dp(n, 0, k+1, goal) % int(1e9 + 7)
