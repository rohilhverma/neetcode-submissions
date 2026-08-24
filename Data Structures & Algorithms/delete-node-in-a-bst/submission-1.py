# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        def help(root):
            if not root.left:
                return root
            return help(root.left)
    
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
            
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        elif key == root.val:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.right and root.left:
                x = help(root.right)
                self.deleteNode(root,x.val)
                root.val = x.val
        return root
            

            