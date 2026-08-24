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
        x = head
        dct={None:None}
        while x:
            dct[x]=Node(x.val, None)
            x=x.next
        x=head

        while x:
            y = dct[x]
            y.next=dct[x.next]
            y.random=dct[x.random]
            x=x.next
        return dct[head]