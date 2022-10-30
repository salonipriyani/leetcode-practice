# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_value):
            if not root:
                return 0
            if root.val >= max_value:
                res = 1
            else:
                res = 0
            max_value = max(max_value, root.val)
                
            res += dfs(root.left, max_value)
            res += dfs(root.right, max_value)
            
            return res
        
        return dfs(root, root.val)