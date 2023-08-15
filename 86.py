from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x: int):
        left = ListNode()
        right = ListNode()
        ret = left
        mid = right
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = mid.next
        return ret.next

    def partition2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        init = ListNode(val=-200)
        init.next = head
        prev = init
        left_node = init
        status = 1
        while head is not None:
            if head.val < x and status:
                left_node = left_node.next
                head = head.next
                prev = prev.next
            elif head.val < x <= prev.val:
                temp1 = head.next
                temp2 = left_node.next
                left_node.next = head
                head.next = temp2
                prev.next = temp1
                head = temp1
                left_node = left_node.next
            elif head.val >= x:
                status = 0
                head = head.next
                prev = prev.next
        return init.next


a = Solution()
data = [[1]]


def build(i, j):
    if i >= len(data[j]): return None
    current = ListNode(data[j][i])
    current.next = build(i + 1, j)
    return current


node = build(0, 0)
x = a.partition2(node, 3)
print(x)
