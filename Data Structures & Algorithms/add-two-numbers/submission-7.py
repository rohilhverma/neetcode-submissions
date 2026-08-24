# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0,None)
        retrn=dummy
        while l1 and l2:
            if l1.val+l2.val+carry>9:
                val = l1.val+l2.val+carry - 10
                carry=1
                dummy.next = ListNode(val, None)
                dummy=dummy.next
            else:
                dummy.next=ListNode(l1.val+l2.val+carry, None)
                carry=0
                dummy=dummy.next
            l1=l1.next
            l2=l2.next
        
        if l2:
            while l2: 
                if l2.val+carry>9:
                    dummy.next =ListNode(l2.val+carry-10, None)
                    carry=1
                    dummy=dummy.next
                else:
                    dummy.next=ListNode(l2.val+carry, None)
                    carry=0
                l2=l2.next
        
        elif l1:
            while l1: 
                if l1.val+carry>9:
                    dummy.next =ListNode(l1.val+carry-10, None)
                    carry=1
                    dummy=dummy.next
                else:
                    dummy.next=ListNode(l1.val+carry, None)
                    carry=0
                l1=l1.next
        
        if carry:
            dummy.next=ListNode(carry, None)
        return retrn.next
                    
                

                
                
                
