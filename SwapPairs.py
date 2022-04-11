"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying 
the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if head==[] or head == None: 
            return head
        if head.next == None: 
            return head
       
        newList = ListNode()
        newList.next = head
        
        #first = head
        #second = first.next
        #rest = second.next
        curr = newList
        while True:
            try:
                first = curr.next
                second = first.next
                rest = second.next
                first.next = rest
                second.next = first
                curr.next = second
                curr = curr.next.next
            except:
                break
        return newList.next
      
