# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        firstHalf,start,end,secondHalf=ListNode(None,head),head,head,None
        returnNode=None
        if k == 1:
            return head

        while True:
            c=1
            for _ in range(k-1):
                if end and end.next:
                    end = end.next
                    c+=1
                else:
                    break
            
            if c == k:
                secondHalf = end.next
                end.next=None
                prev,curr,post=None,start,start
                while curr:
                    post=post.next
                    curr.next=prev
                    prev=curr
                    curr=post
                if not returnNode:
                    returnNode = prev
                
                firstHalf.next=prev
                start.next=secondHalf

                
                start, end, firstHalf = secondHalf,secondHalf, start
            else:
                if returnNode:
                    return returnNode
                return head
