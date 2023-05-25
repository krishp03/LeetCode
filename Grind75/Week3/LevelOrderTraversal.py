# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class LevelOrderTraversal:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []

        q = Queue()
        if root:
            q.put(root)
        while not q.empty():
            level = []

            for i in range(q.qsize()):
                curr = q.get()
                level.append(curr.val)

                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)

            traversal.append(level)

        return traversal
