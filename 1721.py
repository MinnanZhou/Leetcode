# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head, k: int):
        left, right = head, head
        for i in range(1, k):
            left = left.next
        temp = left
        while temp.next:
            temp = temp.next
            right = right.next
        left.val, right.val = right.val, left.val
        return head

    def build_list(self, values):
        head = ListNode(values[0])
        temp = head
        for i in values[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return head


array = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
a = Solution()
linked_list = a.build_list(array)
b = a.swapNodes(linked_list, 8)
while b.next:
    print(b.val)
    b = b.next
