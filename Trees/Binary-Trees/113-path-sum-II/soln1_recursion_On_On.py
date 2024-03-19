# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(root,targetSum,ls,res):
            if root:
                if not root.left and not root.right and targetSum == root.val:
                    ls.append(root.val)
                    res.append(ls)
                dfs(root.left,targetSum-root.val,ls+[root.val],res)
                dfs(root.right,targetSum-root.val,ls+[root.val],res)

        dfs(root,targetSum,[],res)
        return res