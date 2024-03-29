# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if not p and not q:
                return True
            
            if not p:
                return False
            if not q:
                return False
            
            if p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right):
                return True
        
        return dfs(p, q)