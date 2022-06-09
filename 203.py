class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val: int):
        new = ListNode(0)
        ret = new
        while head:
            if head.val != val:
                new.next = head
                new = new.next
            head = head.next
        new.next = None
        return ret.next


a = Solution()
data = [[1, 2, 3, 4, 6, 7, 6]]


def build(i, j):
    if i >= len(data[j]): return None
    current = ListNode(data[j][i])
    current.next = build(i + 1, j)
    return current


node = build(0, 0)
x = a.removeElements(node,6)
print(x)
