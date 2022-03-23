class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head):
        total = 0
        total_list = []
        while head.next is not None:
            total += head.val
            head = head.next
            if total > 0 and head.val == 0:
                total_list.append(total)
                total = 0
        res=None
        total_list.reverse()
        for i in total_list:
            res = ListNode(i, res)
        return res


value = [0,1,0,3,0,2,2,0]
value.reverse()
a = None
for count in value:
    a = ListNode(count, a)

x = Solution()
y = x.mergeNodes(a)
