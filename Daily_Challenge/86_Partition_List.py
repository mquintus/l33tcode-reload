# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = None
        n = head

        greater_start = None
        greater_end = None

        while n is not None:
            #print()
            #print("LEFT LIST", head, "\nRIGHT LIST",greater_start)
            #print(n.val)
            '''
            If the next element is smaller than x,
            it belongs to the left list.

            Do nothing.
            '''
            if n.val < x:
                #print('smaller')
                curr = n
                n = curr.next
                continue

            '''
            If the next element is greater than or equal to x,
            it belongs to the right list.

            Append it to the right list.

            Remove it from the left list.
            '''
            nnext = n.next
            if n.val >= x:
                #print('bigger')
                if greater_start is None:
                    ''' Start the right list with that element '''
                    greater_start = n
                    greater_end = n
                else:
                    ''' Append it to the right list'''
                    #print('Append after', greater_end.val)
                    greater_end.next = n
                    greater_end = n
                '''
                Remove from the left list
                '''
                n = nnext 
                if (curr is not None) and (nnext is not None):
                    curr.next = n
                if curr is None:
                    head = n
                    
            
            if greater_end is not None:
                greater_end.next = None

        ''' Edge cases: If left list is empty or right list is empty... '''
        if curr is not None:
            curr.next = greater_start
        else:
            head = greater_start

        return head
