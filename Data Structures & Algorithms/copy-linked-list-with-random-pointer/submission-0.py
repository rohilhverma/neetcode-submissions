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
        dct = {None: None}
        iterator = head
        while iterator:
            copy = Node(iterator.val)
            dct[iterator] = copy
            iterator = iterator.next
        iterator=head
        while iterator:
            copy = dct[iterator]
            copy.next = dct[iterator.next]
            copy.random = dct[iterator.random]
            iterator=iterator.next
        return dct[head]