# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")
        def dfs(root):
            if root == None:
                return 0
            ls=dfs(root.left)
            if ls < 0:
                ls = 0
            rs=dfs(root.right)
            if rs < 0:
                rs = 0
            self.maxi = max(self.maxi,ls+root.val+rs)
            return root.val + max(ls,rs)
        dfs(root)
        return self.maxi