class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        ret = ListNode(next=ListNode(next=head))
        pointer = ret
        while head and head.next:
            temp = head.next.next
            head.next.next = head
            head = head.next
            head.next.next = temp
            ret.next.next = head
            ret = ret.next.next
            head = head.next.next
        return pointer.next.next


a = Solution()
data = [[1, 2, 3, 4]]


def build(i, j):
    if i >= len(data[j]): return None
    current = ListNode(data[j][i])
    current.next = build(i + 1, j)
    return current


node = build(0, 0)
x = a.swapPairs(node)
print(x)
