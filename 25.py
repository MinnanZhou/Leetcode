class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):
        stack = []
        ret = ListNode()
        pointer = ret
        while head:
            start = head
            while len(stack) < k:
                stack.append(head)
                head = head.next
                if not head: break
            if len(stack) == k:
                while len(stack) > 0:
                    ret.next = stack.pop()
                    ret = ret.next
            else:
                ret.next = start
                return pointer.next
        ret.next = None
        return pointer.next


a = Solution()
data = [[1, 2, 3, 4, 5, 6]]


def build(i, j):
    if i >= len(data[j]): return None
    current = ListNode(data[j][i])
    current.next = build(i + 1, j)
    return current


node = build(0, 0)
x = a.reverseKGroup(node, 4)
print(x)
