# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.lst=[]
    
    def help(self, root):
        if not root:
            return
        self.help(root.left)
        self.lst.append(root.val)
        self.help(root.right)
        
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.help(root)
        return self.lst
