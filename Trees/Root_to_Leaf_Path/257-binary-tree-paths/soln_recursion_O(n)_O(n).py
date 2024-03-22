# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def helper(root,s):
            if not root.left and not root.right:
                res.append(s+str(root.val))
            if root.left:
                helper(root.left,s+str(root.val)+"->")
            if root.right:
                helper(root.right,s+str(root.val)+"->")
        
        helper(root,"")
        return res