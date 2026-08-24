# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        returnNode = dummy=ListNode(None, None)
        while l1 and l2:
            s = l1.val + l2.val + rem 
            if s >= 10:
                rem = (l1.val + l2.val+rem) // 10
            else:
                rem=0
            dummy.next=ListNode(s % 10, None)
            dummy=dummy.next
            l1=l1.next
            l2=l2.next
        
        while l1:
            s = l1.val + rem 
            if s >= 10:
                rem = (l1.val+rem) // 10
            else:
                rem=0
            dummy.next=ListNode(s % 10, None)
            dummy=dummy.next
            l1=l1.next
        
        while l2:
            s = l2.val + rem 
            if s >= 10:
                rem = (l2.val+rem) // 10
            else:
                rem=0
            dummy.next=ListNode(s % 10, None)
            dummy=dummy.next
            l2=l2.next
        if rem:
            dummy.next = ListNode(rem, None)
        
        return returnNode.next
