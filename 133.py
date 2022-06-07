from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new = deque(node.neighbors)
        visited = {node.val}
        links = {node.val: [i.val for i in node.neighbors]}

        while new:
            v = new.popleft()
            if v.val not in visited:
                new += v.neighbors
                visited.add(v.val)
                links[v.val] = [i.val for i in v.neighbors]

        nodes = {}
        for i in list(visited):
            nodes[i] = Node(i)
        for key, value in links.items():
            nodes[key].neighbors = [nodes[k] for k in value]
        return nodes[node.val]


a = Solution()
x = [Node(1), Node(2), Node(3), Node(4)]
x[0].neighbors = [x[1], x[3]]
x[1].neighbors = [x[0], x[2]]
x[2].neighbors = [x[1], x[3]]
x[3].neighbors = [x[0], x[2]]
print(a.cloneGraph(x[0]))
