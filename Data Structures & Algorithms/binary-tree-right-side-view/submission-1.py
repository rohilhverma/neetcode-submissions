# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        q=deque()
        q.append(root)
        while q:
            z = len(q)
            for y in range(len(q)):
                x = q.popleft()
                if not x:
                    continue
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                if y == z-1:
                    l.append(x.val)
        return l