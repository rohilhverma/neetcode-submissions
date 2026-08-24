# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def help(root, tup):
            if not root:
                return (0,0)
            left = help(root.left, tup)
            right = help(root.right, tup)
            return (root.val + left[1]+right[1], max(left)+max(right))
        
        return max(help(root, (0,0)))