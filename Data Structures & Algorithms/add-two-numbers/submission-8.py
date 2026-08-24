# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x=l1
        y=l2
        z=ListNode(0,None)
        dummy=z
        carry=0
        while x and y:
            sum = x.val+y.val+carry
            if sum > 9:
                z.next=ListNode(sum % 10, None)
                z=z.next
                carry=1
            else:
                z.next=ListNode(sum)
                z=z.next
                carry=0
            x=x.next
            y=y.next
        
        while y:
            sum = y.val+carry
            if sum > 9:
                z.next=ListNode(sum % 10,None)
                z=z.next
                carry=1
            else:
                z.next=ListNode(sum)
                z=z.next
                carry=0
            y=y.next
        
        while x:
            sum = x.val+carry
            if sum > 9:
                z.next=ListNode(sum % 10, None)
                z=z.next
                carry=1
            else:
                z.next=ListNode(sum,None)
                z=z.next
                carry=0
            x=x.next
        
        if (carry):
            z.next=ListNode(carry, None)

        return dummy.next
