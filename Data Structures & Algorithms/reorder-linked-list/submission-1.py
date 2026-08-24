# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First break the list into two
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None

        #Reverse this half
        prev=None
        curr=second
        nxt=second
        while curr:
            nxt=nxt.next
            curr.next=prev
            prev=curr
            curr=nxt
        #Work thru this list in reverse
        first=head
        while prev:
            x,y = first.next, prev.next
            first.next=prev
            prev.next=x
            first, prev=x, y

