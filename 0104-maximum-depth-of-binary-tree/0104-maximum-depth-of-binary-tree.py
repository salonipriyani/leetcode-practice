# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 1)
        
    def dfs(self, root, depth):
        if not root:
            return 0
        
        return 1 + max(self.dfs(root.left, depth + 1), self.dfs(root.right, depth + 1))