# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        side_view = []
        
        def helper(root, level):
            if not root:
                return

            if level > len(side_view):
                side_view.append(root.val)

            helper(root.right, level + 1)
            helper(root.left, level + 1)


        helper(root, 1)
        return side_view
      
