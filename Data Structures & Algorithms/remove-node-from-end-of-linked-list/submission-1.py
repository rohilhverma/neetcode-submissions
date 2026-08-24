# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0, head)
        returnDummy=dummy
        toDelete=head
        nAhead=head
        for _ in range(n):
            nAhead=nAhead.next
        
        while nAhead:
            dummy=dummy.next
            toDelete=toDelete.next
            nAhead=nAhead.next
        
        dummy.next=dummy.next.next
        return returnDummy.next
        
        
