# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        def help(root):
            if not root:
                return;
            help(root.left)
            help(root.right)
            lst.append(root.val)
        help(root)
        return lst