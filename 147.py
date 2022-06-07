class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head):
        def insert(node: ListNode, start: ListNode):
            last = None
            ret = start
            while start and node.val > start.val:
                last = start
                start = start.next
            if last:
                last.next = node
                node.next = start
                start = ret
            else:
                node.next = start
                start = node
            return start

        res = head.next
        head.next = None
        while res:
            new = res.next
            res.next = None
            head = insert(res, head)
            res = new
        return head


x = [ListNode(5), ListNode(3), ListNode(2), ListNode(1), ListNode(4)]
for j in range(4):
    x[j].next = x[j + 1]
a = Solution()
print(a.insertionSortList(x[0]))
