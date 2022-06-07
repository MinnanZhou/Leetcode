class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        q = root
        while q:
            if q.left is None and q.right is None:
                q = q.next
                continue
            nextStart = q.left if q.left else q.right
            i = q
            remain = []
            while i:
                if i.left and i.right:
                    if remain:
                        remain.pop().next = i.left
                    i.left.next = i.right
                    remain.append(i.right)
                elif i.left:
                    if remain:
                        remain.pop().next = i.left
                    remain.append(i.left)
                else:
                    if remain:
                        remain.pop().next = i.right
                    remain.append(i.right)
                i = i.next
            q = nextStart
        return root
