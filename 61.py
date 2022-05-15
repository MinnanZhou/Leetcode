class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k: int):
        start = head
        findLength = head
        length = 0
        while findLength and findLength.next:
            length += 1
            findLength = findLength.next
        if length == 0:
            return head
        else:
            length += 1
        k = k % length
        if k == 0:
            return head
        k = length - k
        while k > 0:
            stop = start
            start = start.next
            k -= 1
        findLength.next = head
        stop.next = None
        return start


a = Solution()
data = [[1]]


def build(i, j):
    if i >= len(data[j]): return None
    current = ListNode(data[j][i])
    current.next = build(i + 1, j)
    return current


node = build(0, 0)
x = a.rotateRight(node, 0)
print(x)
