# 2181 - Merge Nodes in Between Zeros
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        orig = head
        adding = True
        collector = head
        prev_collector = head
        curr = collector
        while collector.next is not None:
            curr = collector.next
            while curr.val != 0:
                collector.val += curr.val
                curr = curr.next
            prev_collector = collector
            collector = curr
            prev_collector.next = collector
        prev_collector.next = None
    
        return orig
