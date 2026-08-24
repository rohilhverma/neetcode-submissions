# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.m=-1000 
        def help(root):
            if not root:
                return 0
            
            l = help(root.left)
            r = help(root.right)
            if l < 0:
                l=0
            if r < 0:
                r=0
            self.m = max(self.m, l + r + root.val)
            return root.val + max(l,r)
        return max(help(root), self.m)