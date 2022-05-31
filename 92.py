class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        cache = []
        i = 1
        leftPoint = ListNode()
        rightPoint = None
        if left == 1:
            ret = leftPoint
        else:
            ret = head
        while head and i <= right + 1:
            if i == left - 1:
                leftPoint = head
            elif i == right + 1:
                rightPoint = head
            elif left <= i <= right:
                cache.append(head.val)
            i += 1
            head = head.next
        while cache:
            leftPoint.next = ListNode(cache.pop())
            leftPoint = leftPoint.next
        leftPoint.next = rightPoint
        return ret if left != 1 else ret.next


a = Solution()
data = [[1, 2, 3, 4, 5]]


def build(i, j):
    if i >= len(data[j]): return None
    current = ListNode(data[j][i])
    current.next = build(i + 1, j)
    return current


node = build(0, 0)
x = a.reverseBetween(node, 2, 5)
print(x)
