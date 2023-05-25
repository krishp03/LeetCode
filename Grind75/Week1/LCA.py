# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class LCA:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currVal = root.val
        pVal = p.val
        qVal = q.val

        inBetween = pVal > currVal and qVal < currVal or pVal < currVal and qVal > currVal
        if inBetween or pVal == currVal or qVal == currVal:
            return root
            
        elif pVal > currVal:
            return self.lowestCommonAncestor(root.right, p, q)

        return self.lowestCommonAncestor(root.left, p, q)
