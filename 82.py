class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        start = ListNode(-101)
        start.next = head
        pointer = start
        dup = set()
        while True:
            if head is None:
                pointer.next = head
                break
            if head.next and head.next.val == head.val:
                dup.add(head.val)
            if head.val not in dup:
                pointer.next = head
                pointer = pointer.next
            head = head.next
        return start.next


a = Solution()
data = [[7]]


def build(i, j):
    if i >= len(data[j]): return None
    current = ListNode(data[j][i])
    current.next = build(i + 1, j)
    return current


node = build(0, 0)
x = a.deleteDuplicates(node)
print(x)
