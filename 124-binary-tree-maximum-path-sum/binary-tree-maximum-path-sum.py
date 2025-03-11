# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_path_sum = float('-inf')

        max_path_sum = float('-inf')

        def dfs(root):
            nonlocal max_path_sum
            max_sum = 0
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            max_sum = max(root.val + left, root.val + right, root.val)
            max_path_sum  = max(max_path_sum, max_sum, root.val + left + right)
            return max_sum
            
            
        dfs(root)
        return 0 if max_path_sum == float('-inf') else max_path_sum
            