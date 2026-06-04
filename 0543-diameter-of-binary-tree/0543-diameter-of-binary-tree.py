class Solution:
    def height(self, root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        self.diameter = max(self.diameter, lh + rh)
        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        self.height(root)

        return self.diameter