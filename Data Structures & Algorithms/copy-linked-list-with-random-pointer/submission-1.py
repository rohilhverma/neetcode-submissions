"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dct={None: None}
        firstIterator = head
        secondIterator = head
        while firstIterator:
            dct[firstIterator] = Node(firstIterator.val)
            firstIterator = firstIterator.next
        while secondIterator:
            nodeRef = dct[secondIterator]
            nodeRef.next = dct[secondIterator.next]
            nodeRef.random = dct[secondIterator.random]
            secondIterator = secondIterator.next
        return dct[head]