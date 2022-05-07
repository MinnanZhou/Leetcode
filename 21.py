class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        ret = ListNode()
        res = ret
        while list1 and list2:
            if list1.val <= list2.val:
                ret.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ret.next = ListNode(list2.val)
                list2 = list2.next
            ret = ret.next
        if not list1:
            ret.next = list2
        else:
            ret.next = list1
        return res.next
