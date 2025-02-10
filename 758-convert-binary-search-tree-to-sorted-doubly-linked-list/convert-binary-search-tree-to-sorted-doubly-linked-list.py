"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        first = last = None
        def dfs(node):
            nonlocal first, last
            if node:
                dfs(node.left)
                if last:
                    node.left = last
                    last.right = node
                else:
                    first = node
                last = node
                dfs(node.right)
        if not root:
            return None
        dfs(root)
        first.left = last
        last.right = first
        return first
