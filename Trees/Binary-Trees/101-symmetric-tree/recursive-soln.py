# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and helper(p.left,q.right) and helper(p.right,q.left)
        return helper(root.left,root.right)