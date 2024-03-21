# 206 - Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        pre_prev = None
        while head is not None:
            pre_prev = prev
            prev = head
            head = head.next
            prev.next = pre_prev
            
        return prev

            
