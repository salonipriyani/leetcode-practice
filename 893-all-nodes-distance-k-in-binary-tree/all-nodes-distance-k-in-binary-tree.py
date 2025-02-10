# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # create a parent map
        # check left, right and parent of target at k radius

        parent_map = {}

        def dfs(node, parent):
            if not node:
                return
            parent_map[node] = parent

            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        res = []
        visited = set()
        def get_k_dist_nodes(node, radius):
            if not node or radius > k or node in visited:
                return
            visited.add(node)
            if radius == k:
                res.append(node.val)
            get_k_dist_nodes(node.left, radius + 1)
            get_k_dist_nodes(node.right, radius + 1)
            get_k_dist_nodes(parent_map[node], radius + 1)

        get_k_dist_nodes(target, 0)
        return res