# 143 - Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find mid
        slow = head
        fast = head
        while fast is not None:
            prev = slow
            fast = fast.next
            slow = slow.next
            if fast is not None:
                fast = fast.next
        
        # Reverse
        prev.next = None
        prev = None
        while slow is not None:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            if nextNode is None:
                break
            slow = nextNode

        # Merge
        while head is not None and slow is not None:
            headNext = head.next
            head.next = slow
            slowNext = slow.next
            slow.next = headNext
            head = headNext
            slow = slowNext
