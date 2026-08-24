# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        dq = deque()
        if not root:
            return lst
        dq.append(root)   
        while dq:
            l = []
            for x in range(len(dq)):
                y = dq.popleft()
                if not y:
                    continue
                if y.left:
                    dq.append(y.left)
                if y.right:  
                    dq.append(y.right)
                l.append(y.val)
            lst.append(l)
        return lst