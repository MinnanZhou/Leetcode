class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None, pos=0):
        self.val = int(x)
        self.next = next
        self.random = random
        self.pos = pos


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        links = {}
        nodes = []
        i = 0
        start = head
        while start:
            start.pos = i
            i += 1
            start = start.next
        i = 0
        while head:
            nodes.append(Node(head.val))
            links[i] = head.random.pos if head.random is not None else head.random
            head = head.next
            i += 1
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i + 1]
            nodes[i].random = nodes[links[i]] if links[i] is not None else None
        nodes[-1].random = nodes[links[len(nodes)-1]] if links[len(nodes)-1] is not None else None
        return nodes[0]
