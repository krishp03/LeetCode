# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class DiameterOfBinaryTree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_diameter = 0
        def max_depth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            nonlocal max_diameter

            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)

            if left_depth + right_depth > max_diameter:
                max_diameter = left_depth + right_depth

            return 1 + max(left_depth, right_depth)

        max_depth(root)
        return max_diameter
      
