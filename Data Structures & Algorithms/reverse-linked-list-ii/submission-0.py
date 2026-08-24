# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        retrn=dummy
        count=1
        l=head
        r=head

        while l and r and count != left:
            l=l.next
            r=r.next
            dummy=dummy.next
            count+=1
        while r and count != right:
            r=r.next
            count+=1
        
        dummy.next=None
        secondHalf = r.next
        r.next=None

        prev=None
        curr=l
        post=l
        while curr:
            post=post.next
            curr.next=prev
            prev=curr
            curr=post
        
        dummy.next, l.next = prev, secondHalf

        return retrn.next
        

        
        
