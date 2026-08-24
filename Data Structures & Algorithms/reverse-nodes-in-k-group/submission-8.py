# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy, curr, ahead = ListNode(None, head), head, head
        returnNode = dummy
        def help(node):
            prev, curr, post = None, node, node
            while curr:
                post=post.next
                curr.next=prev
                prev=curr
                curr=post
            return prev        
        
        while True:
            for x in range(k-1):
                if not ahead:
                    return returnNode.next
                ahead=ahead.next
            if not ahead:
                return returnNode.next
            temp = ahead.next
            ahead.next = None

            # head of new reverse list
            new = help(curr)
            # point tail to remainder of list
            curr.next = temp
            #point previous list to head of reverse list
            dummy.next = new

            ahead=temp
            dummy=curr
            curr=ahead

        
        return returnNode.next

            
            

            
