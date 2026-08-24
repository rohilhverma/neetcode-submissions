# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        x=head
        y=head

        if (head == None or head.next == None):return
        while y and y.next:
            x=x.next
            y=y.next.next
        
        z=x.next
        x.next=None

        prev=None
        curr=z
        post=z
        while curr:
            post=post.next
            curr.next=prev
            prev=curr
            curr=post
        
        a=head

        while prev:
            post1,post2=a.next,prev.next

            a.next=prev
            prev.next=post1

            a,prev = post1,post2
        

        
        