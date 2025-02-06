# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = collections.deque()
        q.append([root, 0])
        col_map = {}
        min_col, max_col = 0, 0
        while q:
            print(col_map)
            curr, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if col not in col_map:
                col_map[col] = []
            col_map[col].append(curr.val)
            if curr.left is not None:
                q.append([curr.left, col - 1])
            if curr.right is not None:
                q.append([curr.right, col + 1])
        res_ls = []
        for i in range(min_col, max_col + 1):
            res_ls.append(col_map[i])
        return res_ls


