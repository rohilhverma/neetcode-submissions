# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def help(root, sum):
            if root:
                sum += root.val

                if not root.left and not root.right:
                    if sum == targetSum:
                        return True
                        
                else:
                    if help(root.left, sum):
                        return True
                    if help(root.right, sum):
                        return True
                sum -= root.val
            return False

        return help(root, 0)