class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def MSort(self, head1, head2):
        # Merge Sort
        if not head1 and not head2:
            return None
        elif head1 and head2:
            if head1.val < head2.val:
                sort = head1
                head1 = head1.next
            else:
                sort = head2
                head2 = head2.next
        else:
            sort = head1 if head1 else head2
        ret = sort
        while head1 and head2:
            if head1.val < head2.val:
                sort.next = head1
                head1 = head1.next
            else:
                sort.next = head2
                head2 = head2.next
            sort = sort.next
        if head1:
            sort.next = head1
        else:
            sort.next = head2
        return ret

    def sortList(self, head):
        if not head or not head.next:
            return head
        fast = head.next.next
        slow = head.next
        last = None
        while fast and fast.next:
            fast = fast.next.next
            last = slow
            slow = slow.next
        if last:
            last.next = None
        else:
            head.next = None
        return self.MSort(self.sortList(head), self.sortList(slow))


x = [ListNode(0), ListNode(1), ListNode(4), ListNode(2), ListNode(3), ListNode(10), ListNode(4), ListNode(5),
     ListNode(6), ListNode(8)]
for j in range(9):
    x[j].next = x[j + 1]
a = Solution()
y = a.sortList(x[0])
print(y)
