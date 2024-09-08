# 725 - Split Linked List in Parts
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def size(node):
            if node is None:
                return 0
            return 1 + size(node.next)
        length = size(head)

        chunk = length // k
        extra = length % k

        chunks = []
        chunks.append(head)
        node = head
        for i in range(1,k):
            if node is None:
                chunks.append(None)
                continue
            currchunk = chunk
            if extra > 0:
                currchunk += 1
                extra -= 1
            for j in range(currchunk - 1):
                node = node.next
            chunks.append(node.next)
            node.next = None
            node = chunks[-1]
        return chunks
            

