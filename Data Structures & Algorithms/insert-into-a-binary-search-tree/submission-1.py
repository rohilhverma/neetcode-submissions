# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, val):
        if not root:
            root = TreeNode(val)
            return root
        if root.val < val:
            root.right = self.helper(root.right, val)
        elif root.val > val:
            root.left = self.helper(root.left, val)
        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        return self.helper(root, val)