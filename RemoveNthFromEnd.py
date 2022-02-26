# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
        '''
        # Need to find the length of the list
        length = 1
        node = head
        while node.next:
            length +=1
            node = node.next
        if length <= 1:
            return
        if n==length:
            head = head.next
            return head
        node = head
        posn = 0
        # Need to remove elelment at position len - n
        # which means reattaching elelemtn at len - n -1
        removeAt = length - n -1
        while posn < removeAt:
            posn += 1
            node = node.next
        node.next = node.next.next
        
        return head
