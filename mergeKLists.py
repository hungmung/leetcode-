# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ptr = head = ListNode()
        if len(lists)==0: return None      # Empty list
        if len(lists)==1: return lists[0]  # Only one list
        
        
        # Join all the lists
        for ll in lists:
            ptr.next = ll
            while ptr.next != None:
                ptr = ptr.next
        ptr = head
        if ptr.next==None: return None
        lo = ptr.next
        hi = lo.next
        if hi == None: return lo
        while lo.next != None:
            if lo.val <= hi.val:
                lo = lo.next
                hi = hi.next
            else:
                # Need to swap
                tmp = lo.val
                lo.val = hi.val
                hi.val = tmp
                lo = head.next
                hi = lo.next
        return head.next
