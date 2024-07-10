# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        s1 = []
        s2 = []
        s1.append(root)
        while s1 or s2:
            level = []
            while s1:
                n = s1.pop()
                level.append(n.val)
                if n.left:
                    s2.append(n.left)
                if n.right:
                    s2.append(n.right)
            if level:
                res.append(level)
            level = []
            while s2:
                n = s2.pop()
                level.append(n.val)
                if n.right:
                    s1.append(n.right)
                if n.left:
                    s1.append(n.left)
            if level:
                res.append(level)
        return res
