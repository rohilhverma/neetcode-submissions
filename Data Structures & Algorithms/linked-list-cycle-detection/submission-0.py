# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        if head == None:
            return False
        while (head.next != None):
            hashset.add(head)
            if (head.next in hashset):
                return True
            head = head.next
        return False
        