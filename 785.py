class Solution:
    def isBipartite(self, graph) -> bool:
        partition = [-1 for _ in range(len(graph))]
        partition[0] = 0
        visited = set([i for i in range(len(partition))])
        i = 0
        stack = []
        while len(visited) > 0:
            links = graph[i]
            visited.remove(i)
            nextPart = 0 if partition[i] == 1 else 1
            for node in links:
                stack.append(node)
                if partition[node] == nextPart:
                    continue
                elif partition[node] == -1:
                    partition[node] = nextPart
                else:
                    return False
            while stack and stack[-1] not in visited:
                stack.pop()
            if stack:
                i = stack.pop()
            else:
                if not visited:
                    break
                i = visited.pop()
                visited.add(i)
        return True


a = Solution()
inp = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(a.isBipartite(inp))
