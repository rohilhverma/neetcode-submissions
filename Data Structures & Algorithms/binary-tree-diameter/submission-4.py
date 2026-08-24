# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.globalVal=0
        def help(root):
            if not root:
                return 0
            l, r = help(root.left), help(root.right)
            self.globalVal=max(self.globalVal, l + r)
            return 1 + max(l, r)
        help(root)
        return self.globalVal