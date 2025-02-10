"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        
        def dfs(node):
            if not node:
                return None
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        if not node:
            return None
        return dfs(node)

