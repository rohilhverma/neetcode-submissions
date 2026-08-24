# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x, y = ListNode(0,head),head
        returnDummy=x

        for _ in range(n):
            y=y.next
        
        while y:
            x,y=x.next,y.next
        x.next=x.next.next
        return returnDummy.next