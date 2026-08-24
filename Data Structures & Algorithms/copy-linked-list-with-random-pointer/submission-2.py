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
        dct={None:None}
        x = head
        while x:
            dct[x] = Node(x.val, None, None)
            x=x.next
        y=head
        while y:
            nde=dct[y]
            nde.next=dct[y.next]
            nde.random=dct[y.random]
            y=y.next
        return dct[head]