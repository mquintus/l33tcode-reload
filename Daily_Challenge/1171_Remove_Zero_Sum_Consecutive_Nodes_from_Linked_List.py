# 1171 - Remove Zero Sum Consecutive Nodes from Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Delete all nodes after prev and including node
        def deleteNode(head, node, prev):
            if node == head:
                #print("Node is head")
                head = head.next
            elif prev is not None:
                #print("Prev not None")
                prev.next = node.next
            elif prev is None:
                #print("Prev is None")
                head = node.next
            return head

        node = head   
        while head is not None and node is not None:
            #print(head)
            node = head
            prev = None
            vals = []
            vals2 = []
            while node is not None:
                #print(vals2)
                needs_refresh = False
                if node.val == 0:
                    prev = None
                    if len(vals):
                        prev = vals[-1][0]
                    head = deleteNode(head, node, prev)
                    needs_refresh = True
                    break

                vals.append([node, 0])
                vals2.append(0)
                
                for i in range(len(vals)):
                    vals[i][1] += node.val
                    vals2[i] += node.val

                    if vals[i][1] == 0:
                        if i > 0:
                            prev = vals[i-1][0]
                        head = deleteNode(head, node, prev)
                        needs_refresh = True
                        break

                node = node.next

                if needs_refresh:
                    break
        return head
