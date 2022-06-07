class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        visited = set()
        while headA or headB:
            if headA == headB:
                return headA
            if headA in visited:
                return headA
            if headB in visited:
                return headB
            if headA is not None:
                visited.add(headA)
                headA = headA.next
            if headB is not None:
                visited.add(headB)
                headB = headB.next
        return None
