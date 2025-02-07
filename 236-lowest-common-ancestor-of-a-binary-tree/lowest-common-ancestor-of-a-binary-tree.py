# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        common = None
        def dfs(node):
            nonlocal common
            if not node:
                return False
            left = right = mid = False
            if node == p or node == q:
                mid = True
            left = dfs(node.left)
            right = dfs(node.right)
            if mid + left + right >= 2:
                common = node
            return left or right or mid
        dfs(root)
        return common