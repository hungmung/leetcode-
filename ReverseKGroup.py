# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        newHead = ListNode()
        newHead.next = head
        curr = newHead
        ptr = newHead
        kGroup = []
        while True:
            try:
                print (ptr)
                for i in range(k):
                    kGroup.append(ptr.next)
                    ptr = ptr.next
                rest = ptr.next
                for x in kGroup[::-1]:
                    curr.next = x
                    curr = curr.next
                curr.next = rest
                kGroup.clear()
            except:
                break
                
        return newHead.next
