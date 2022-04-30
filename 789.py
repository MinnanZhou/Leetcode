class Solution:
    def escapeGhosts(self, ghosts, target) -> bool:
        def manDis(p0, p1):
            return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])

        human = manDis([0, 0], target)
        return all(manDis(g, target) > human for g in ghosts)
