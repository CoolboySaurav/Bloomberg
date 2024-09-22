# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = temp = ListNode(0)
        
        while l1 or l2:
            a = b = float('inf')
            if l1: 
                a = l1.val
            if l2:
                b = l2.val 
            if a < b:
                temp.next = l1
                l1 = l1.next 
            else:
                temp.next = l2
                l2 = l2.next 
            temp = temp.next
        
        return dummy.next