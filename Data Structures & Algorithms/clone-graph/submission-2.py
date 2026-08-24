"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque, defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dct={}
        first = second = node
        q1, q2 = deque(), deque()
        q1.append(first)
        q2.append(second)
        if not node:
            return
        while q1:
            temp = q1.popleft()
            dct[temp] = Node(temp.val)
            for x in temp.neighbors:
                if x not in dct:
                    q1.append(x)
        visit=set()
        while q2:
            temp = q2.popleft()
            if temp in visit:
                continue
            visit.add(temp)
            for x in temp.neighbors:
                dct[temp].neighbors.append(dct[x])
                q2.append(x)
            
        return dct[node]

