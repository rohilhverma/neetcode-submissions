# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d=0
        if not root:return 0

        def help(root, d):
            if not root:
                return d
            else:
                return max(help(root.left,d + 1),help(root.right,d+ 1))

        return help(root,d)