# 2487 - Remove Nodes From Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodevals = []
        node = head
        while node is not None:
            nodevals.append(node.val) 
            node = node.next
        
        greatest = [nodevals[-1]]
        for val in nodevals[-2::-1]:
            if val < greatest[-1]:
                greatest.append(greatest[-1])
            else:
                greatest.append(val)
        greatest = greatest[::-1]
        
        # Find the new head
        node = head
        p = 0
        while node.val < greatest[p]:
            head = node.next
            node = head
            p += 1

        # Remove other nodes
        node = head
        prev = node
        while node is not None:
            if node.val < greatest[p]:
                prev.next = node.next
            else:
                prev = node
            p += 1
            node = node.next
            
        
        return head

        
