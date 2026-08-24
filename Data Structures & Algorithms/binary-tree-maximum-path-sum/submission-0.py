# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        lst=[]
        def help(root):
            if not root:
                return 0
            left = help(root.left)
            right = help(root.right)
            if left < 0:
                left=0
            if right < 0:
                right=0
            if root.left and root.right:
                lst.append(root.val + left + right)
                return root.val + max(left, right)
            elif root.left:

                lst.append(root.val+left)
                return root.val + left
            else:
                lst.append(root.val+right)
                return root.val + right
        help(root)
        return max(lst)