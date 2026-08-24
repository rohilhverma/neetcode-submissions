# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l,r=head,head
        dummy=ListNode(0,head)
        returnDummy=dummy
        left-=1
        right-=1
        while left:
            dummy=dummy.next
            l=l.next
            r=r.next
            left-=1
            right-=1
        while right:
            r=r.next
            right-=1
        
        dummy.next=None
        rightHalf = r.next
        r.next=None

        prev,curr,post=None,l,l
        while curr:
            post=post.next
            curr.next=prev
            prev=curr
            curr=post
        
        dummy.next=prev
        l.next=rightHalf

        return returnDummy.next
    

        
