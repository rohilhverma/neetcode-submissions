# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        laggingPointer = dummy
        aheadPointer = head
        while n:
            n -= 1
            aheadPointer = aheadPointer.next
            
        while aheadPointer:
            aheadPointer = aheadPointer.next
            laggingPointer = laggingPointer.next
        laggingPointer.next = laggingPointer.next.next
        return dummy.next