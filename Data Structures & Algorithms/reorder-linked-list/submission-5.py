# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 1
        x = head
        while x:
            x=x.next
            l+=1
        
        l = math.ceil(l / 2)
        left = x = head
        while x:
            l-=1
            if l == 0:
                right = x.next
                x.next=None
                break
            x = x.next


        right,curr,post = None, right, right
        while curr:
            post=post.next
            curr.next=right
            right=curr
            curr=post
        
        while right and left:
            newLeft, newRight = left.next, right.next

            left.next = right
            right.next = newLeft

            left, right = newLeft, newRight
