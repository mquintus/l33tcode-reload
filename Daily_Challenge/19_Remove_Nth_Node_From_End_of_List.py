# 19 - Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length(root):
            if root is None:
                return 0
            return 1 + get_length(root.next)
        length = get_length(head)
        prev_node = None
        curr_node = head
        target_position = length - n
        
        # Edge case: return the first node
        if target_position == 0:
            head = head.next
            return head

        # Normal case: the `head` stays the same
        while target_position > 0:
            target_position -= 1
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = curr_node.next
        return head
        
