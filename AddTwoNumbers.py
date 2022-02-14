# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sz_l1=""
        sz_l2=""
        while True:
            sz_l1 += str(l1.val)
            l1 = l1.next
            if l1==None:break
        while True:
            sz_l2 += str(l2.val)
            l2 = l2.next
            if l2==None:break
        i_l1=int(sz_l1[::-1])
        i_l2=int(sz_l2[::-1])
        op = str(i_l1+i_l2)[::-1]
        l = ListNode(op[0])
        current = l
        for char in op[1:]:
            current.next = ListNode(char)
            current = current.next
        return l
