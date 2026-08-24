# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l=deque()
        r=deque()
        l.append(p)
        r.append(q)
        while l and r:
            if len(l) != len(r):
                return False
            for x in range(len(l)):
                a=l.popleft()
                b=r.popleft()
                if not a and not b:
                    continue
                if not a or not b:
                    return False
                if a.val != b.val:
                    return False
                l.append(a.left)
                l.append(a.right)
                r.append(b.left)
                r.append(b.right)
        return True