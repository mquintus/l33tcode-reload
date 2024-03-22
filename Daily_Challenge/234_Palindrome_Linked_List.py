# 234 - Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def count(node):
            counter = 0
            while node.next is not None:
                node = node.next
                counter += 1
            return counter
        def getNodeByNumber(node, counter):
            while counter >= 0 and node.next is not None:
                node = node.next
                counter -= 1
            return node
        def reverseList(node):
            prev = None
            while node is not None:
                nextNode = node.next
                node.next = prev
                prev = node
                if nextNode is None:
                    break
                node = nextNode
            return node

        length = count(head)

        midnode = getNodeByNumber(head, length // 2)
        #print(midnode)
        rightSide = reverseList(midnode)
        #print(rightSide)

        while rightSide is not None and head is not None:
            if rightSide.val != head.val:
                return False
            rightSide = rightSide.next
            head = head.next
        return True

