# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        def count_list_length(head):
            counter = 0
            while head is not None:
                counter += 1
                head = head.next
            return counter
        
        length = count_list_length(head)

        avg = length / k

        shorter_length = int(avg)

        longer_length = shorter_length

        if avg > shorter_length:
            longer_length += 1

        longer_count = (length % k)

        list_of_heads = []
        while len(list_of_heads) < k:
            longer_count -= 1

            list_of_heads.append(head)

            if longer_count >= 0:
                n = longer_length
            else:
                n = shorter_length

            prev = head
            if n == 0:
                head = None
            while n > 0:
                prev = head
                if head is not None:
                    head = head.next
                n -= 1
            
            if prev is not None:
                prev.next = None

        return list_of_heads

            
