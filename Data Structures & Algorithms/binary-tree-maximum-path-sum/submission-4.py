class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = float("-inf")
        def help(root):
            if not root:
                return 0
            
            l = max(help(root.left), 0)
            r = max(help(root.right), 0)

            self.m = max(l + r + root.val, self.m)
            return root.val + max(l, r)
        help(root)
        return self.m