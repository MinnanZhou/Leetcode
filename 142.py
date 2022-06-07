class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        start = head
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                slow = slow.next
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start
            slow = slow.next
            fast = fast.next.next
        return None


x = [ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)]
for i in range(4):
    x[i].next = x[i + 1]
# x[4].next = x[4]
a = Solution()
print(a.detectCycle(x[0]))
