# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        returnNode = dummy=ListNode(None, head)
        x = node = head
        l=0
        while x:
            l+=1
            x=x.next
        
        while l != n:
            l-=1
            node=node.next
            dummy=dummy.next
        dummy.next = dummy.next.next

        return returnNode.next
        


