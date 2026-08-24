# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        
        y=None 
        curr=second
        post=second
        while curr:
            post=post.next
            curr.next=y
            y=curr
            curr=post

        first, second = head, y
        while second:
            x, y = first.next, second.next
            first.next=second
            second.next=x
            first, second = x, y
        

            



        