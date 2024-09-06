# 3217 - Delete Nodes From Linked List Present in Array
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        prev = head
        curr = head.next
        while curr is not None:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        if head.val in nums:
            head = head.next
        return head
