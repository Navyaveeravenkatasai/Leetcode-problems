class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def height(root):
            if root == None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            self.diameter = max(self.diameter,lh+rh)

            return 1 + max(lh,rh)

        height(root)

        return self.diameter