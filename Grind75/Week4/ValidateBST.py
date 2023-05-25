# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class ValidateBST:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], min: Optional[int], max: Optional[int]) -> bool:
            if not root:
                return True
            if max is not None and root.val >= max:
                return False
            if min is not None and root.val <= min:
                return False

            return helper(root.left, min, root.val) and helper(root.right, root.val, max)
    
        return helper(root, None, None)
