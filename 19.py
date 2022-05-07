class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        temp = head
        ret = head
        while head.next:
            if n > 0:
                n -= 1
                head = head.next
            else:
                temp = temp.next
                head = head.next
        if n == 1:
            return ret.next
        else:
            temp.next = temp.next.next
            return ret


a = Solution()
data = [1, 2, 3, 4]


def build(i):
    if i >= len(data): return None
    current = ListNode(data[i])
    current.next = build(i + 1)
    return current


node = build(0)
x = a.removeNthFromEnd(node, 4)
print(a.removeNthFromEnd(node, 2))
