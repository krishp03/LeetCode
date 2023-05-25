# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BalancedBinaryTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            lheight, rheight = helper(root.left), helper(root.right)
            if lheight == -1 or rheight == -1 or abs(lheight - rheight) > 1:
                return -1
            
            return max(lheight, rheight) + 1

        return helper(root) != -1
