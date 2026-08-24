# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        node = head
        while node:
            if node.next not in hashset:
                hashset.add(node)
            else:
                return True
            node = node.next
        return False