# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        x, y = head,head.next

        while y and y.next:
            x=x.next
            y=y.next.next
        
        half = x.next
        x.next=None

        prev,curr,post=None,half,half
        while curr:
            post=post.next
            curr.next=prev
            prev=curr
            curr=post
        
        x = head
        while x and prev:
            a, b, c, d = x, x.next, prev, prev.next

            a.next=c
            c.next = b

            x = b
            prev = d
        

