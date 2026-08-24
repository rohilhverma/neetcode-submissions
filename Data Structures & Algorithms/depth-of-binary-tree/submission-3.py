# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def help(root, val):
            if not root:
                return val-1
            l, r = help(root.left, val+1), help(root.right, val+1)
            return max(l,r)
        
        return help(root, 1)