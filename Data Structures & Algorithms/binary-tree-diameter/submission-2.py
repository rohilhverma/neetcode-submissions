# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.m = 0

        def help(root):
            if not root: 
                return 0
            
            x = help(root.left)
            y = help(root.right)
            self.m = max(x + y, self.m)
            return 1 + max(x, y)

        help(root)
        return self.m