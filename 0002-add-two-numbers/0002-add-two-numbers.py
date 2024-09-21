# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = temp = ListNode(0)
        carry = 0
        tot = 0
        
        while l1 or l2:
            a = b = 0
            if l1:
                a = l1.val 
                l1 = l1.next 
            if l2:
                b = l2.val 
                l2 = l2.next
            tot = (a + b + carry) % 10
            carry = (a + b + carry) // 10 
            temp.next = ListNode(tot)
            temp = temp.next 
        if carry:
            temp.next = ListNode(carry)
        
        return dummy.next
            