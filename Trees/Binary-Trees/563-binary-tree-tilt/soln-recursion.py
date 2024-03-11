# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        def sum(root):
            nonlocal ans
            if root is None:
                return 0
            leftSum = sum(root.left)
            rightSum = sum(root.right)
            ans += abs(leftSum - rightSum)
            return root.val + leftSum + rightSum
        
        sum(root)
        return ans
