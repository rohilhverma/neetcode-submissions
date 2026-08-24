# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.globalVal = -1000
        def help(root):
            if not root:
                return 0
            
            l, r = help(root.left), help(root.right)
            if l < 0:
                l = 0
            if r < 0:
                r = 0

            self.globalVal = max(self.globalVal, root.val+l+r)
            return root.val + max(l, r)
        return max(help(root), self.globalVal)
            