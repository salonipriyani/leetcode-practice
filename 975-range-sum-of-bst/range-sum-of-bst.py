# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_incl = 0

        def dfs(node):
            sum = 0
            if not node:
                return 0
            if node.val >= low and node.val <= high:
                sum += node.val
            sum += dfs(node.left)
            sum += dfs(node.right)
            return sum
        return dfs(root)