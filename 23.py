import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        hp = []
        chain = ListNode()
        ret = chain
        for i, linked in enumerate(lists):
            if linked:
                heapq.heappush(hp, (linked.val, i))
                lists[i] = lists[i].next
        while hp:
            curr = heapq.heappop(hp)
            chain.next = ListNode(curr[0])
            if lists[curr[1]]:
                heapq.heappush(hp, (lists[curr[1]].val, curr[1]))
                lists[curr[1]] = lists[curr[1]].next
            chain = chain.next
        return ret.next


a = Solution()
data = [[1, 4, 5], [1, 3, 4], [2, 6], []]


def build(i, j):
    if i >= len(data[j]): return None
    current = ListNode(data[j][i])
    current.next = build(i + 1, j)
    return current


node = [build(0, k) for k in range(len(data))]
x = a.mergeKLists(node)
print(x)
