# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_total = 0
        def dfs(node, sum):
            nonlocal sum_total
            if not node:
                return 0
            
            sum = (sum * 10) + node.val
            if not (node.left or node.right):
                sum_total += sum

            dfs(node.left, sum)
            dfs(node.right, sum)
        
        dfs(root, 0)
        return sum_total