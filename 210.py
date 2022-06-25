class Node:
    def __init__(self, val):
        self.courseNo = val
        self.prevCourse = []


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
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
            ret.append(node)
            dp[node] = True
            return True

        unfinished = {i: Node(i) for i in range(numCourses)}
        head = set(unfinished.keys())
        for pairs in prerequisites:
            unfinished[pairs[1]].prevCourse.append(pairs[0])
            if pairs[0] in head: head.remove(pairs[0])
        if not head: return []
        dp = [-1 for _ in range(numCourses)]
        ret = []
        while head:
            start = head.pop()
            dfs(start, set())
        return ret[::-1] if all(d is True for d in dp) else []


a = Solution()
inp = [[1,0],[2,0],[3,1],[3,2]]
print(a.findOrder(4, inp))
