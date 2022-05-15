from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dq = [root, None]
        nextLevel = []
        while dq:
            for i in range(len(dq) - 1):
                if dq[i]:
                    dq[i].next = dq[i + 1]
                    if dq[i].left:
                        nextLevel.append(dq[i].left)
                    if dq[i].right:
                        nextLevel.append(dq[i].right)
            dq = nextLevel.copy() + [None]
            nextLevel.clear()
        return root
