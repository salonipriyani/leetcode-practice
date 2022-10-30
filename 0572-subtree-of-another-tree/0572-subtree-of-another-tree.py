# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root:
                return False
            
            if not subRoot:
                return True
            
            if helper(root, subRoot):
                print(1)
                return True
            else:
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        def helper(p, q):
            if not p and not q:
                return True
            if not p:
                return False
            if not q:
                return False
            if p.val == q.val and helper(p.left, q.left) and helper(p.right, q.right):
                return True
            return False
        return dfs(root, subRoot)
            
            