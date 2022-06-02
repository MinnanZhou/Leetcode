class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head):
        data = []
        while head:
            data.append(head.val)
            head = head.next
        n = len(data)

        def build(start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(data[start])
            mid = (start + end) // 2
            root = TreeNode(data[mid])
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)
            return root

        return build(0, n - 1)
