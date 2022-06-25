class Node:
    def __init__(self, val):
        self.courseNo = val
        self.prevCourse = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        def dfs(node, path):
            if dp[node] != -1: return dp[node]
            if node in path:
                dp[node] = False
                return False
            path.add(node)
            for n in unfinished[node].prevCourse:
                if not dfs(n, path):
                    dp[node] = False
                    return False
            path.remove(node)
            dp[node] = True
            return True

        unfinished = {i: Node(i) for i in range(numCourses)}
        head = set(unfinished.keys())
        for pairs in prerequisites:
            unfinished[pairs[1]].prevCourse.append(pairs[0])
            if pairs[0] in head: head.remove(pairs[0])
        if not head: return False
        dp = [-1 for _ in range(numCourses)]
        while head:
            start = head.pop()
            if not dfs(start, set()): return False
        return True if all(d != -1 for d in dp) else False


a = Solution()
inp = [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]]
print(a.canFinish(8, inp))
