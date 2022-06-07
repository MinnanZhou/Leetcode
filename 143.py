class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        n = len(nodes)
        index = []
        for i in range(n // 2):
            index += [i, n - i - 1]
        if n % 2 == 1: index.append(n // 2)
        for i in range(n - 1):
            nodes[index[i]].next = nodes[index[i + 1]]
        nodes[index[-1]].next = None


x = [ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)]
for j in range(4):
    x[j].next = x[j + 1]
a = Solution()
print(a.reorderList(x[0]))
