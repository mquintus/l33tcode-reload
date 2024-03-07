# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_length(root):
            if root is None:
                return 0
            return 1 + get_length(root.next)
        length = get_length(head)
        target = (length // 2)
        for _ in range(target):
            head = head.next
        return head
